from torch import nn
from torch.optim import adam 
from torch .utils.data import  DataLoader
from torchvision import datasets 
from torchvision.transformer import TOTensor

train = datasets.MNIST(root = "data, dowload=True, train=True, transform=ToTensor)
dataset = DataLoader(train, 32)
                       
                       