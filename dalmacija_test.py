import os
from torch.utils.data import DataLoader

from utils.midi_utils import read_midi_file
from utils.melody_dataset import MelodyDataset

medjimurje_dataset_folder = 'res/dataset/dalmacija/'

dataset = MelodyDataset(medjimurje_dataset_folder)
dataloader = DataLoader(dataset=dataset, batch_size=4, shuffle=True, num_workers=0)
for melody in dataloader:
    print(melody.shape)