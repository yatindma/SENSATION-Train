import random

import numpy as np
import torch

# color mapping for classes
CLASS_COLOR_MAP = np.array([
    (165, 42, 42),
    (0, 192, 0),
    (196, 196, 196),
    (190, 153, 153),
    (180, 165, 180),
    (90, 120, 150),
    (102, 102, 156),
    (128, 64, 255),
    (140, 140, 200),
    (170, 170, 170),
    (250, 170, 160),
    (96, 96, 96),
    (230, 150, 140),
    (128, 64, 128),
    (110, 110, 110),
    (244, 35, 232),
    (150, 100, 100),
    (70, 70, 70),
    (150, 120, 90),
    (220, 20, 60),
    (255, 0, 0),
    (255, 0, 100),
    (255, 0, 200),
    (200, 128, 128),
    (255, 255, 255),
    (64, 170, 64),
    (230, 160, 50),
    (70, 130, 180),
    (190, 255, 255),
    (152, 251, 152),
    (107, 142, 35),
    (0, 170, 30),
    (255, 255, 128),
    (250, 0, 30),
    (100, 140, 180),
    (220, 220, 220),
    (220, 128, 128),
    (222, 40, 40),
    (100, 170, 30),
    (40, 40, 40),
    (33, 33, 33),
    (100, 128, 160),
    (142, 0, 0),
    (70, 100, 150),
    (210, 170, 100),
    (153, 153, 153),
    (128, 128, 128),
    (0, 0, 80),
    (250, 170, 30),
    (192, 192, 192),
    (220, 220, 0),
    (140, 140, 20),
    (119, 11, 32),
    (150, 0, 255),
    (0, 60, 100),
    (0, 0, 142),
    (0, 0, 90),
    (0, 0, 230),
    (0, 80, 100),
    (128, 64, 64),
    (0, 0, 110),
    (0, 0, 70),
    (0, 0, 192),
    (32, 32, 32),
    (120, 10, 10),
    (0, 0, 0)
])

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "mps")
Trained_model = torch.load("Pytorch_Weights/DeeplabV3Plus_resnet101.pth", map_location=DEVICE)
Trained_model.to(DEVICE)
Trained_model.eval()


def preprocessing_fn(img):
    img = img / 255.0
    img = img - np.array([0.485, 0.456, 0.406])
    img = img / np.array([0.229, 0.224, 0.225])
    return img.astype(np.float32)

def decode_segmentation_map(mask, nc=21):
    rgb = CLASS_COLOR_MAP[mask]
    return rgb.astype(np.uint8)

# def decode_segmentation_map(mask, nc=21):
#     label_colors = np.array(
#         [(0, 0, 0)] + [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(nc)])
#     r = np.zeros_like(mask).astype(np.uint8)
#     g = np.zeros_like(mask).astype(np.uint8)
#     b = np.zeros_like(mask).astype(np.uint8)
#     for l in range(0, nc):
#         idx = mask == l
#         r[idx] = label_colors[l, 0]
#         g[idx] = label_colors[l, 1]
#         b[idx] = label_colors[l, 2]
#     rgb = np.stack([r, g, b], axis=2)
#     return rgb
