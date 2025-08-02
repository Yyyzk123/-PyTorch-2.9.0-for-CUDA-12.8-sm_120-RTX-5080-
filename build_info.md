# 🔧 PyTorch Build Information

This file documents the technical details of the PyTorch 2.9.0 build for CUDA 12.8 + sm_120 (RTX 5080 Ada architecture).

---

## ✅ Build Metadata

| Key               | Value                                     |
|------------------|-------------------------------------------|
| PyTorch Version   | 2.9.0a0                                   |
| Git Commit Hash   | gitc665594                                |
| CUDA Version      | 12.8.0                                    |
| cuDNN Version     | 8.9 (system-installed)                    |
| Architecture      | sm_120 (Ada Lovelace / RTX 5080 Laptop)  |
| Python Version    | 3.10.x (Conda environment)                |
| Platform          | Ubuntu 24.04 LTS (x86_64)                 |
| Build Date        | 2025-08-02                                |
| Build Machine     | Intel i9-14900HX + NVIDIA RTX 5080 Laptop GPU |

---

## 🛠 Build Configuration Flags

- `USE_CUDA=1`
- `USE_DISTRIBUTED=1`
- `USE_MKLDNN=1`
- `USE_NCCL=1`
- `USE_CUDNN=1`
- `TORCH_CUDA_ARCH_LIST="12.0"`

---

## 🧪 Verification Tasks

- [x] Gaussian Splatting (train & render)
- [x] SplaTAM (RGB-D + mapping)
- [x] Tensor CUDA check (examples/demo_tensor_cuda.py)

---

## 📁 Output File

