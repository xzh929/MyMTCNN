from PIL import Image
import cv2
import torch
import numpy as np
from torchvision import transforms as t

img = Image.open(r"F:\imgdata\52.jpg")
w, h = img.size
max_size = np.max((h, w))
min_size = np.min((h, w))
if max_size == h:
    img_mask = t.Pad([(max_size - min_size), 0, 0, 0])(img)
else:
    img_mask = t.Pad([0, (max_size - min_size), 0, 0, ])(img)
img_mask.show()
print(img.size)
print(img_mask.size)
