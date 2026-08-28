import cv2
import numpy as np
import torch
from ultralytics import YOLO

print("=== AI Robot Vision Environment ===")
print("Python environment: OK")
print("NumPy:", np.__version__)
print("OpenCV:", cv2.__version__)
print("PyTorch:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
print("Ultralytics: OK")
print("\nEnvironment setup successful!")