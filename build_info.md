# 🔧 PyTorch Build Information

This file documents the technical details of the custom-built PyTorch 2.9.0 (CUDA 12.8 + sm_120) optimized for Ada Lovelace (RTX 5080 Laptop GPU).

---

## ✅ Build Metadata

| Key               | Value                                               |
|------------------|-----------------------------------------------------|
| PyTorch Version   | 2.9.0a0                                             |
| Git Commit Hash   | gitc665594                                          |
| CUDA Version      | 12.8.61                                             |
| cuDNN Version     | Not installed (runtime-only container)             |
| Architecture      | sm_120 (Ada Lovelace / RTX 5080 Laptop GPU)        |
| Python Version    | 3.10.18 (via Conda)                                 |
| Platform          | Ubuntu 24.04 LTS (x86_64)                           |
| Build Date        | 2025-08-02                                          |
| Build Machine     | Intel i9-14900HX + NVIDIA RTX 5080 Laptop GPU       |

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
- [x] `examples/demo_tensor_cuda.py` (Tensor CUDA validation)

---

## 📦 Output Artifact

- `torch-2.9.0a0+gitc665594-cp310-cp310-linux_x86_64.whl`

---

## 📁 Reproduction Environment

For full reproducibility, see [`requirements.txt`](./requirements.txt)
