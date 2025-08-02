# PyTorch 2.9.0 for CUDA 12.8 + sm_120 (RTX 5080)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![CUDA 12.8](https://img.shields.io/badge/CUDA-12.8-success.svg)](https://developer.nvidia.com/cuda-downloads)
[![PyTorch 2.9.0](https://img.shields.io/badge/PyTorch-2.9.0-orange)](https://pytorch.org/)
[![GitHub stars](https://img.shields.io/github/stars/Yyyzk123/pytorch-cuda128-sm120?style=social)](https://github.com/Yyyzk123/pytorch-cuda128-sm120)

## Overview
This repository provides a pre-built PyTorch 2.9.0 package compiled with CUDA 12.8 and `sm_120` architecture, targeting RTX 5080 Laptop GPUs (Ada Lovelace).
该项目提供适配 CUDA 12.8 + sm_120 架构（RTX 5080）的 PyTorch 2.9.0 编译版本，已通过 Gaussian Splatting、SplaTAM 等实际任务验证。欢迎反馈问题或提交 PR！

## 🚀 Quick Start (3 Steps)
```bash
# Step 1: Download
wget https://github.com/Yyyzk123/pytorch-cuda128-sm120/releases/download/v2.9.0-sm120/torch-2.9.0a0+sm120-cuda128-cp310-cp310-linux_x86_64.whl

# Step 2: Install
pip install torch-2.9.0a0+sm120-cuda128-cp310-cp310-linux_x86_64.whl

# Step 3: Verify
python -c "import torch; print(torch.__version__); print(torch.cuda.get_device_name(0))"
``` 

## Features
- ✅ Built from source: PyTorch v2.9.0 + gitc665594
- ✅ CUDA 12.8 compatible
- ✅ Supports `sm_120` (RTX 5080, Ada Lovelace)
- ✅ Python 3.10 environment
- ✅Verified on real-world AI pipelines (Gaussian Splatting, SplaTAM)

## Requirements 
- Linux x86_64（建议 Ubuntu 22.04）
- Python 3.10（推荐使用 Conda）
- CUDA 12.8 已安装（NVIDIA 驱动 >= 550）
- NVIDIA GPU 支持 sm_120（例如 RTX 5080）
- pip >= 21.0
> ⚠️ **Warning**  
> Make sure your CUDA path is correctly set:  
> 
> ```bash
> export PATH=/usr/local/cuda-12.8/bin:$PATH
> export LD_LIBRARY_PATH=/usr/local/cuda-12.8/lib64:$LD_LIBRARY_PATH
> ```

## Tested on
- ✅ PyTorch GPU Acceleration (verified)
- ✅ Gaussian Splatting
- ✅ SplaTAM

## Installation
```bash
   wget https://github.com/Yyyzk123/pytorch-cuda128-sm120/releases/download/v2.9.0-sm120/torch-2.9.0a0+sm120-cuda128-cp310-cp310-linux_x86_64.whl
   pip install torch-2.9.0a0+sm120-cuda128-cp310-cp310-linux_x86_64.whl
```
