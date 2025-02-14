import numpy as np
import torch
from denoising_diffusion_pytorch import Unet1D, GaussianDiffusion1D, Trainer1D, Dataset1D
from utils.melody_helpers import generate_maj_scale, write_melody_to_wav


def z_score_normalize(tensor):
    mean = torch.mean(tensor)
    std = torch.std(tensor)
    return (tensor - mean) / std

def min_max_normalize(tensor, min, max):
    return (tensor - min)/(max - min)

def rescale_melody(tensor, min, max):
    return tensor * (max - min) + min


model = Unet1D(
    dim = 64,
    dim_mults = (1, 2, 4, 8),
    channels = 1 
)

diffusion = GaussianDiffusion1D(
    model,
    seq_length = 8,
    timesteps = 100,
    objective = 'pred_v'
)

# training_seq = torch.rand(64, 32, 128) # features are normalized from 0 to 1
# custom dataset - major scales
MIN_KEY, MAX_KEY = 1, 88
MELODY_LENGTH = 8
N_SAMPLES = 64
# make it integer instead of float
keys = np.random.randint(low=MIN_KEY, high=MAX_KEY-MELODY_LENGTH, size=N_SAMPLES)
dataset = torch.from_numpy(np.array([generate_maj_scale(key) for key in keys], dtype=np.float32))
dataset = min_max_normalize(dataset, MIN_KEY, MAX_KEY) 

# loss = diffusion(training_seq)
# loss.backward()

# Or using trainer

# dataset = Dataset1D(training_seq)  # this is just an example, but you can formulate your own Dataset and pass it into the `Trainer1D` below
dataset = Dataset1D(torch.unsqueeze(dataset, 1))
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(f"Device: {device}")
trainer = Trainer1D(
    diffusion,
    dataset = dataset,
    train_batch_size = 32,
    train_lr = 8e-5,
    train_num_steps = 600,         # total training steps
    gradient_accumulate_every = 2,    # gradient accumulation steps
    ema_decay = 0.995,                # exponential moving average decay
    amp = True,                       # turn on mixed precision
)
trainer.train()

# after a lot of training

sampled_seq = diffusion.sample(batch_size = 4)
sampled_seq.shape # (4, 32, 128)
print(f"Sampled seq raw: {sampled_seq}")
melodies = rescale_melody(torch.squeeze(sampled_seq).detach().cpu(), MIN_KEY, MAX_KEY)
print(f"Melodies: {melodies}")

for i in range(len(torch.squeeze(melodies))):
    write_melody_to_wav(melody=melodies[i], output_file=f"output_melody{i}.wav")