# PyTorch 2.9.0 for CUDA 12.8 + sm_120 (RTX 5080)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![CUDA 12.8](https://img.shields.io/badge/CUDA-12.8-success.svg)](https://developer.nvidia.com/cuda-downloads)
[![PyTorch 2.9.0](https://img.shields.io/badge/PyTorch-2.9.0-orange)](https://pytorch.org/)
[![GitHub stars](https://img.shields.io/github/stars/Yyyzk123/pytorch-cuda128-sm120?style=social)](https://github.com/Yyyzk123/pytorch-cuda128-sm120)

## 🚀 Overview
This repository provides a pre-built PyTorch 2.9.0 package compiled with CUDA 12.8 and `sm_120` architecture, targeting RTX 5080 Laptop GPUs (Ada Lovelace).
该项目提供适配 CUDA 12.8 + sm_120 架构（RTX 5080）的 PyTorch 2.9.0 编译版本，已通过 Gaussian Splatting、SplaTAM 等实际任务验证。欢迎反馈问题或提交 PR！
> 🐧 **Tested on Ubuntu 22.04 / 24.04 (Linux x86_64)**  
> Compatible with Ubuntu-based systems (including WSL2). Other Linux distributions may require manual setup.

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
- ✅ Supports `sm_120` (RTX 5080, Ada Lovelace)
- ✅ Python 3.10 environment
- ✅ Verified on real-world AI pipelines (Gaussian Splatting, SplaTAM)

## 📋 Requirements
- Linux x86_64 (Recommended: Ubuntu 22.04)
- Python 3.10 (Conda environment recommended)
- CUDA 12.8 installed (NVIDIA driver >= 550)
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

## 🐛 Found a Bug or Have a Feature Request?
We're happy to improve this repo with you!
- 👉 [Submit a Bug Report](https://github.com/Yyyzk123/YOUR_REPO_NAME/issues/new?template=bug_report.yaml)
- ✨ [Request a Feature](https://github.com/Yyyzk123/YOUR_REPO_NAME/issues/new?template=feature_request.yaml)
> Please check [CONTRIBUTING.md](CONTRIBUTING.md) before submitting.

## 📓 Changelog
See [CHANGELOG.md](./CHANGELOG.md) for update history. 
## 🙌 Contributing
We welcome issues, PRs, or feedback!
Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.  

## 👉 See [build_info.md](./build_info.md) for full build details (OS, CUDA, commit hash, etc).

