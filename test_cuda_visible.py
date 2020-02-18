import torch

import os
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID" # see issue #152
os.environ["CUDA_VISIBLE_DEVICES"]="4"

a = torch.zeros((1000,1000,1000)).cuda()
b = torch.zeros((1000,1000,1000)).cuda()
