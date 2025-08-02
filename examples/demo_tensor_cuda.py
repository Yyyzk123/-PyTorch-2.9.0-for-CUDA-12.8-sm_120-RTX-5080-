# examples/demo_tensor_cuda.py

import torch
import sys

print("Verifying PyTorch CUDA tensor operations...\n")
print("-----------------------------------------")
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")

# Check CUDA availability
if not torch.cuda.is_available():
    print("[ERROR] CUDA not available. Please check your installation:")
    print("  1. Download CUDA 12.8: https://developer.nvidia.com/cuda-downloads")
    print("  2. Install and restart your terminal")
    sys.exit(1)

# Perform tensor operations on GPU
device = torch.device("cuda")
print(f"Using GPU: {torch.cuda.get_device_name(device)}")

x = torch.ones((3, 3), dtype=torch.float32).to(device)
y = torch.rand((3, 3), dtype=torch.float32).to(device)
z = x + y

print("\nInput Tensor X (ones):")
print(x)
print("\nInput Tensor Y (random):")
print(y)
print("\nOutput Tensor Z = X + Y:")
print(z)
print("-----------------------------------------")
print("[SUCCESS] Tensor operation on GPU completed!")
print("Believe in light!")
