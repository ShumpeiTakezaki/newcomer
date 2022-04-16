# i try to build resnet50 from scratch (but, i will use model.resnet....)
import torch
import torch.nn as nn
import torch.functional as F


class ResBlock(nn.Module):
    def __init__(self, in_f, f_1, out_f, stride=1):
        super(ResBlock, self).__init__()
        self.stride = stride
        self.fit_dim = False

        self.block = nn.Sequential(
            nn.Conv2d(in_f, f_1, kernel_size=1, padding=0, stride=stride),
            nn.BatchNorm2d(f_1),
            nn.ReLU(),
            nn.Conv2d(f_1, f_1, kernel_size=3, padding=1, stride=1),
            nn.BatchNorm2d(f_1),
            nn.ReLU(),
            nn.Conv2d(f_1, out_f, kernel_size=1, padding=0, stride=1),
            nn.BatchNorm2d(out_f),
            nn.ReLU()
        )

        if in_f != out_f:
            self.fit_conv = nn.Conv2d(in_f, out_f, kernel_size=1, padding=0, stride=stride)
            self.fit_bn = nn.BatchNorm2d(out_f)
            self.fit_dim = True

        self.relu = nn.ReLU()
        
    def forward(self, x):
        res_x = self.block(x)

        if self.fit_dim:
            x = self.fit_conv(x)
            x = self.fit_bn(x)
            x = self.relu(x)
        
        x += res_x
        x = self.relu(x)
        return x

class ResNet50(nn.Module):
    def __init__(self, out_class):
        super(ResNet50, self).__init__()
        self.out_class = out_class

        self.module = nn.Sequential(
                nn.Conv2d(3, 64, kernel_size=7, padding=3, stride=2),
                nn.BatchNorm2d(64),
                nn.ReLU(),
                nn.MaxPool2d([3,3], padding=1, stride=2),
                ResBlock(64, 64, 256), # ResBlock2
                ResBlock(256, 64, 256),
                ResBlock(256, 64, 256),
                ResBlock(256, 128, 512, stride=2), # ResBlock3
                ResBlock(512, 128, 512),
                ResBlock(512, 128, 512),
                ResBlock(512, 128, 512),
                ResBlock(512, 256, 1024, stride=2), # ResBlock 4
                ResBlock(1024, 256, 1024),
                ResBlock(1024, 256, 1024),
                ResBlock(1024, 256, 1024),
                ResBlock(1024, 256, 1024),
                ResBlock(1024, 256, 1024),
                ResBlock(1024, 512, 2048, stride=2), # ResBlock 5
                ResBlock(2048, 512, 2048),
                ResBlock(2048, 512, 2048)
            )
        
        self.gap = nn.AdaptiveAvgPool2d((1,1))
        self.fc = nn.Linear(2048, self.out_class)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.module(x) 
        x = self.gap(x)
        x = self.fc(x)
        x = self.sigmoid(x)
        
        return x