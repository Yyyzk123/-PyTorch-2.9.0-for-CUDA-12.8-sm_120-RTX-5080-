# 🤝 Contributing to PyTorch 2.9.0 (CUDA 12.8 + sm_120)

Welcome! 👋 We appreciate your interest in contributing to this project.

This project provides a pre-built PyTorch 2.9.0 package for CUDA 12.8 with sm_120 (Ada, RTX 5080) support. Verified on Gaussian Splatting, SplaTAM, and more.

---

## 📦 How to Contribute Code

### 1. Fork the Repository
Click the `Fork` button at the top right of this page.

### 2. Clone Your Fork
```bash
git clone https://github.com/YOUR_USERNAME/pytorch-cuda128-sm120.git
cd pytorch-cuda128-sm120
```

### 3. Create a New Branch
```bash
git checkout -b feature/your-feature-name
```

### 4. Make Your Changes
If you’re modifying build scripts or configs, please also:
> Run build_pytorch.sh to ensure .whl builds successfully.
> Run examples/verify_install.py to confirm installation is correct.

### 5. Commit and Push
```bash
git add .
git commit -m "Add: describe your change clearly"
git push origin feature/your-feature-name
```
### 6. Open a Pull Request
Go to your fork → Switch to your branch → Click “Compare & Pull Request”

📚 Code Style & Guidelines
✅ Use clear, concise commit messages
✅ Add comments if modifying scripts
✅ Don't commit .whl or large binary files
✅ Keep README.md and build_info.md in sync if relevant

🐞 Reporting Issues
Please open an issue and include:
System info (nvidia-smi, nvcc --version)
Error logs (full stack trace if any)
Steps to reproduce (optional but helpful)

🙌 Thanks for Your Contribution!
Let’s build a faster and better CUDA PyTorch experience together 💪


