import torch
import sys

print("Verifying PyTorch installation...\n")
print(f"Torch version: {torch.__version__}")
print(f"CUDA version : {torch.version.cuda}")

# Check CUDA version
EXPECTED_CUDA = "12.8"
if not torch.version.cuda.startswith(EXPECTED_CUDA):
    print(f"WARNING: Expected CUDA {EXPECTED_CUDA}, but got {torch.version.cuda}")
    sys.exit(1)

# Check GPU availability and architecture
if torch.cuda.is_available():
    try:
        for i in range(torch.cuda.device_count()):
            name = torch.cuda.get_device_name(i)
            cc = torch.cuda.get_device_capability(i)
            print(f"GPU {i}: {name}")
            print(f"Compute Capability: {cc}")
            if cc == (12, 0):
                print("✔ Architecture OK: sm_120 (RTX 5080 compatible)")
            else:
                print(f"WARNING: Not sm_120! Detected {cc}, may be incompatible.")
        print("\nAll checks passed. You're ready to accelerate AI!")
    except Exception as e:
        print(f"Error while checking GPU: {e}")
        sys.exit(1)
else:
    print("ERROR: No GPU detected.")
    print("Make sure NVIDIA driver and CUDA 12.8 are properly installed:")
    print("1. Download: https://developer.nvidia.com/cuda-downloads")
    print("2. Install and restart your terminal")
    sys.exit(1)
