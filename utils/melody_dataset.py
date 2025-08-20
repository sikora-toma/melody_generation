import torch
from torch.utils.data import Dataset, DataLoader
import os

from utils.midi_utils import read_midi_file


MIN_KEY, MAX_KEY = 1, 88
MEAN_DURATION, STD_DURATION = 765, 446

class MelodyDataset(Dataset):
    def __init__(self, dataset_path, sample_len=8, tranform=None):
        self.dataset_path = dataset_path
        self.files = [file for file in os.listdir(dataset_path) if '.mid' in file]
        self.sample_len = sample_len
        self.transform = tranform
    
    def __getitem__(self, index):
        sample = read_midi_file(self.dataset_path + self.files[index], return_tensor=True)
        sample = self.normalize(sample[:,:self.sample_len])
        if self.transform:
            sample = self.transform(sample)
        return sample
    
    def __len__(self):
        return len(self.files)
    
    def normalize(self, sample):
        sample[0] = (sample[0] - MIN_KEY)/(MAX_KEY - MIN_KEY)
        sample[1] = (sample[1] - MEAN_DURATION)/STD_DURATION
        return sample

    def rescale(self, sample):
        sample[0] = sample[0] * (MAX_KEY - MIN_KEY) + MIN_KEY
        sample[1] = sample[1] * STD_DURATION + MEAN_DURATION
        return sample


class Modulate(object):
    def __call__(self, sample):
        minimum, maximum = torch.min(sample[0]), torch.max(sample[0])
        value = torch.randint(low=MIN_KEY-int(minimum*(MAX_KEY-MIN_KEY)+MIN_KEY), high=MAX_KEY-int(maximum*(MAX_KEY-MIN_KEY)+MIN_KEY), size=(1,))
        # print(value, minimum*(MAX_KEY-MIN_KEY), maximum*(MAX_KEY-MIN_KEY))
        assert minimum+value/(MAX_KEY-MIN_KEY)>=-0.01 and maximum+value/(MAX_KEY-MIN_KEY)<=1.01, f"Mistake in melody minimum and maximum calculation. {minimum+value/(MAX_KEY-MIN_KEY)} {maximum+value/(MAX_KEY-MIN_KEY)}"
        sample[0]+=torch.ones(sample.shape[-1])*(value/(MAX_KEY-MIN_KEY))
        return sample
    
class TimeScale(object):
    def __init__(self, std=0.01) -> None:
        self.std = std
    def __call__(self, sample):
        value = torch.normal(0.0,self.std, (1,))
        sample[1]+=torch.ones(sample.shape[-1])*value
        return sample
 

if __name__=='__main__':
    dataset = MelodyDataset('../res/dataset/medjimurje/')
    dataloader = DataLoader(dataset=dataset, batch_size=4, shuffle=True, num_workers=0)
    print(dataset.__len__())