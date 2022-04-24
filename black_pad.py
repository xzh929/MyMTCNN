from PIL import Image
import cv2
import torch
import numpy as np
from torchvision import transforms as t

def black_pad(path):
    img = Image.open(path)
    w, h = img.size
    max_size = np.max((h, w))
    min_size = np.min((h, w))
    if max_size == h:
        img_mask = t.Pad([(max_size - min_size), 0, 0, 0])(img)
    else:
        img_mask = t.Pad([0, (max_size - min_size), 0, 0, ])(img)
    return img_mask


if __name__ == '__main__':
    img_path = r"F:\imgdata\52.jpg"
    img = Image.open(img_path)
    img_blackpad = black_pad(img_path)
    img_blackpad.show()
    print(img.size)
    print(img_blackpad.size)
