import torch
from torch.utils.data import Dataset, DataLoader
import os

from utils.midi_utils import read_midi_file
from utils.melody_helpers import min_max_normalize


MIN_KEY, MAX_KEY = 1, 88
MEAN_DURATION, STD_DURATION = 765, 446

class MelodyDataset(Dataset):
    def __init__(self, dataset_path, sample_len=8):
        self.dataset_path = dataset_path
        self.files = [file for file in os.listdir(dataset_path) if '.mid' in file]
        self.sample_len = sample_len
    
    def __getitem__(self, index):
        tensor = read_midi_file(self.dataset_path + self.files[index], return_tensor=True)
        return self.normalize(tensor[:,:self.sample_len])
    
    def __len__(self):
        return len(self.files)
    
    def normalize(self, tensor):
        tensor[0] = (tensor[0] - MIN_KEY)/(MAX_KEY - MIN_KEY)
        tensor[1] = (tensor[1] - MEAN_DURATION)/STD_DURATION
        return tensor



if __name__=='__main__':
    dataset = MelodyDataset('../res/dataset/medjimurje/')
    dataloader = DataLoader(dataset=dataset, batch_size=4, shuffle=True, num_workers=0)
    print(dataset.__len__())