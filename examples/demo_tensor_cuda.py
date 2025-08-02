# examples/demo_tensor_cuda.py

import torch
import sys

print("🧪 Verifying PyTorch CUDA tensor operations...\n")
print("────────────────────────────────────────────")
print(f"🧠 PyTorch version: {torch.__version__}")
print(f"⚙️ CUDA available: {torch.cuda.is_available()}")

if torch.cuda.is_available():
    device = torch.device("cuda")
    print(f"✅ Using GPU: {torch.cuda.get_device_name(device)}")
else:
    device = torch.device("cpu")
    print("⚠️ CUDA not available. Running on CPU instead.")

# Perform tensor operations on selected device
x = torch.ones((3, 3), dtype=torch.float32).to(device)
y = torch.rand((3, 3), dtype=torch.float32).to(device)
z = x + y

print("\n📦 Input Tensor X (ones):")
print(x)
print("\n📦 Input Tensor Y (random):")
print(y)
print("\n📦 Output Tensor Z = X + Y:")
print(z)

print("────────────────────────────────────────────")
print(f"[SUCCESS] Tensor operation completed on: {device.type.upper()}")
print("Believe in light! 🌟")
