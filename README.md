# PyTorch 2.9.0 for CUDA 12.8 + sm_120 (RTX 5080)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![CUDA 12.8](https://img.shields.io/badge/CUDA-12.8-success.svg)](https://developer.nvidia.com/cuda-downloads)
[![PyTorch 2.9.0](https://img.shields.io/badge/PyTorch-2.9.0-orange)](https://pytorch.org/)
[![GitHub stars](https://img.shields.io/github/stars/Yyyzk123/pytorch-cuda128-sm120?style=social)](https://github.com/Yyyzk123/pytorch-cuda128-sm120)

> ⚡ **Prebuilt PyTorch + torchvision for Ada GPUs (e.g., RTX 5080)**  
> 🔧 **Built for CUDA 12.8 · Fully Offline Install · Verified in Gaussian Splatting / SplaTAM**  
> 😣 **Feedback & Issues**: Use [GitHub Issues](https://github.com/Yyyzk123/pytorch-cuda128-sm120/issues)  
> 🙌 **Contribute**: See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines

---
## 🚀 Quick Start （3 Steps)
---
### 📥 Step 1: Download `.whl` files

| Package      | Version (tag)         | File Size | SHA256                                     |
|--------------|------------------------|-----------|---------------------------------------------|
| [`torch`](https://github.com/Yyyzk123/torch-cu128-sm120/releases/download/v2.9.0-sm120/torch-2.9.0a0+gitc665594-cp310-cp310-linux_x86_64.whl) | 2.9.0a0+gitc665594 | 235 MB   | `d8534c88263d8f184afea91dfc4feaf8ee2038ce526861a9f8868e716f8a158` |
| [`torchvision`](https://github.com/Yyyzk123/torch-cu128-sm120/releases/download/v2.9.0-sm120/torchvision-0.24.0a0+f52c4f1-cp310-cp310-linux_x86_64.whl) | 0.24.0a0+f52c4f1   | 1.87 MB  | `40655e9c93425751e400de656f0c0ceb81383bfbe4f392edce5b56458892fb9f` |


### 💽 Step 2:  environment

```bash
conda create -n torch_env python=3.10 -y
conda activate torch_env

pip install ./torch-2.9.0a0+gitc665594-cp310-cp310-linux_x86_64.whl
pip install ./torchvision-0.24.0a0+f52c4f1-cp310-linux_x86_64.whl
```

### ✅ Step 3: Verify 
```bash
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"
```
---
### 📌 Check
```bash
2.9.0a0+gitc665594
True
NVIDIA GeForce RTX 5080 Laptop GPU
```

---

## 📂 Project Structure
```
├── .github/                       # GitHub workflows & issue templates
│ ├── workflows/
│ │ └── test-install.yml           # CI workflow: test install from .whl
│ └── ISSUE_TEMPLATE/
│   ├── bug_report.yaml            # Issue template: bug report
│   ├── config.yml                 # Issue template config
│   └── feature_request.yaml       # Issue template: feature request
│
├── examples/
│ ├── demo_tensor_cuda.py          # Demo: test tensor on GPU
│ └── verify_install.py            # Verifies torch installation & CUDA
│
├── scripts/
│ ├── build_pytorch.sh              # Script to build PyTorch from source
│ └── upload_release.py             # Helper to upload .whl to GitHub release
│
├── requirements.txt                # Python dependency list (no torch)
├── install_from_whl.sh             # One-line installer using .whl
├── build_info.md                   # Build config & environment metadata
├── CHANGELOG.md                    # Version history
├── CONTRIBUTING.md                 # Contribution guidelines
├── LICENSE                         # License (MIT/Apache/etc.)
├── .gitignore                      # Git ignored files
└── README.md                       # Project overview & installation guide
```


## 📓 Changelog
- 👉 See [CHANGELOG.md](./CHANGELOG.md) for update history. 
- 👉 See [build_info.md](./build_info.md) for full build details (OS, CUDA, commit hash, etc).

