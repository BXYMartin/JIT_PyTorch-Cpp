import torch
import torchvision
from torchvision import transforms
from PIL import Image
from time import time
import numpy as np

# read image
image = Image.open('dog.png').convert('RGB')
default_transform = transforms.Compose([
        transforms.Resize([224, 224]),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
      ])
image = default_transform(image)

unified_output = image.unsqueeze(0)
with open('bfile.bin', 'wb') as f: 
	f.write(unified_output.data.numpy())

print("Finished Output.")
