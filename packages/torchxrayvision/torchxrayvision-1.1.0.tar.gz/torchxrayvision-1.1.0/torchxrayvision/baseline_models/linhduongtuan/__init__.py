import sys, os
thisfolder = os.path.dirname(__file__)
sys.path.insert(0, thisfolder)
import json
import pathlib
import torch
import torch.nn as nn
import torchvision


import torch.nn as nn


class EfficientNet(nn.Module):
    def __init__(self, apply_sigmoid=True):

        super(EfficientNet, self).__init__()

        import onnx
        from onnx2pytorch import ConvertModel

        print("Errors are normal when loading this model")
        onnx_model = onnx.load(f'{thisfolder}/EfficientNet_B1_240.pth')
        pytorch_model = ConvertModel(onnx_model).eval()

        self.apply_sigmoid = apply_sigmoid

        self.model = pytorch_model
        self.upsample = nn.Upsample(size=(384, 384), mode='bilinear', align_corners=False)

        self.normalize = torchvision.transforms.Normalize(0.55001191, 0.18854326)

        self.targets = ['HCC18', 'HCC22', 'HCC85', 'HCC96', 'HCC108', 'HCC111', 'AGE', 'RAF', 'BMI', 'A1C']

    def forward(self, x):
        x = x.repeat(1, 3, 1, 1)
        x = self.upsample(x)

        # XRV -> 01
        x = (((x / 1024) + 1) / 2)

        x = self.normalize(x)

        y = self.model(x)

        # if self.apply_sigmoid:
        #     y = torch.sigmoid(y)

        return y

    def __repr__(self):
        return "duly_health-DenseNet"


import sys
import requests

# from here https://sumit-ghosh.com/articles/python-download-progress-bar/


def download(url, filename):
    with open(filename, 'wb') as f:
        response = requests.get(url, stream=True)
        total = response.headers.get('content-length')

        if total is None:
            f.write(response.content)
        else:
            downloaded = 0
            total = int(total)
            for data in response.iter_content(chunk_size=max(int(total / 1000), 1024 * 1024)):
                downloaded += len(data)
                f.write(data)
                done = int(50 * downloaded / total)
                sys.stdout.write('\r[{}{}]'.format('█' * done, '.' * (50 - done)))
                sys.stdout.flush()
    sys.stdout.write('\n')

