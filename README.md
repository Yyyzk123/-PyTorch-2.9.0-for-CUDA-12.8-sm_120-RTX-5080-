# PyTorch 2.9.0 for CUDA 12.8 + sm_120 (RTX 5080)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![CUDA 12.8](https://img.shields.io/badge/CUDA-12.8-success.svg)](https://developer.nvidia.com/cuda-downloads)
[![PyTorch 2.9.0](https://img.shields.io/badge/PyTorch-2.9.0-orange)](https://pytorch.org/)
[![GitHub stars](https://img.shields.io/github/stars/Yyyzk123/pytorch-cuda128-sm120?style=social)](https://github.com/Yyyzk123/pytorch-cuda128-sm120)

## 🚀 Overview
This repository provides a pre-built PyTorch 2.9.0 package compiled with CUDA 12.8 and `sm_120` architecture, targeting RTX 5080 Laptop GPUs (Ada Lovelace).
该项目提供适配 CUDA 12.8 + sm_120 架构（RTX 5080）的 PyTorch 2.9.0 编译版本，已通过 Gaussian Splatting、SplaTAM 等实际任务验证。欢迎反馈问题或提交 PR！
> 🐧 **Tested on Ubuntu  24.04 (Linux x86_64)**  
> Compatible with Ubuntu-based systems (including WSL2). Other Linux distributions may require manual setup.
>Follow me. The Windows version will be updated soon...

## 🧪 Quick Install (3 Steps)
```bash
# Step 1: Download
wget https://github.com/Yyyzk123/pytorch-cuda128-sm120/releases/download/v2.9.0-sm120/torch-2.9.0a0+gitc665594-cp310-cp310-linux_x86_64.whl

# Step 2: Install
pip install torch-2.9.0a0+gitc665594-cp310-cp310-linux_x86_64.whl

# Step 3: Verify
python examples/verify_install.py       # or examples/demo_tensor_cuda.py

# (Optional) Step 4: Run example verification script
python examples/demo_tensor_cuda.py
```

## 🔧 Build from Source
If you want to compile from source (e.g. custom patch, cross-platform), run:
```bash
bash scripts/build_pytorch.sh
```
The script builds PyTorch with CUDA 12.8, targets sm_120, and writes the resulting .whl to dist/.

## ✨ Features
- ✅ Built from source: PyTorch v2.9.0 + gitc665594
- ✅ CUDA 12.8 compatible
- ✅ Supports sm_120 (RTX 5080, Ada Lovelace)
- ✅ Verified on Ubuntu 24.04 + Python 3.10.18
- ✅ Matched with torchvision==0.24.0a0+f52c4f1
- ✅ Reproducible environment defined in requirements.txt

## 📋 Requirements
- Linux x86_64 (Recommended: Ubuntu 24.04)
- Python 3.10.18 (via Miniconda or virtualenv)
- CUDA 12.8 installed (NVIDIA Driver ≥ 570.153.02)
- NVIDIA GPU supporting `sm_120` (e.g., RTX 5080 Laptop)
- pip >= 21.0
> ⚠️ **Warning**  
> Make sure your CUDA path is correctly set:  
> 
> ```bash
> export PATH=/usr/local/cuda-12.8/bin:$PATH
> export LD_LIBRARY_PATH=/usr/local/cuda-12.8/lib64:$LD_LIBRARY_PATH
> ```

## 🧪 Tested on
- ✅ PyTorch GPU Acceleration (verified)
- ✅ Gaussian Splatting
- ✅ SplaTAM

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

## 📦 Release Files
You can download pre-built wheels from the GitHub Releases Page.
Latest version: 
[torch-2.9.0a0+gitc665594-cp310-cp310-linux_x86_64.whl]
(https://github.com/Yyyzk123/pytorch-cuda128-sm120/releases/download/v2.9.0-sm120/torch-2.9.0a0+gitc665594-cp310-cp310-linux_x86_64.whl)
⚠️Note: This PyTorch .whl depends on glibc >= 2.38 and can only run on systems with Ubuntu 24.04 or higher.
It is recommended to use the nvidia/cuda:12.8.0-runtime-ubuntu24.04 image for deployment.

## 📓 Changelog
See [CHANGELOG.md](./CHANGELOG.md) for update history. 

## 🙌 Contributing
- Feedback and issues are welcome via [GitHub Issues](https://github.com/Yyyzk123/pytorch-cuda128-sm120/issues)
Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.  

## 👉 See [build_info.md](./build_info.md) for full build details (OS, CUDA, commit hash, etc).

