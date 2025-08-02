#!/bin/bash
# install_from_whl.sh - Install PyTorch 2.9.0 (CUDA 12.8 + sm_120) in 3 steps!
# Author: Yyyzk123 | Updated: 2025-08-02
# Mission: Self-launch platform for AI engineers and beginners. Zero-failure, max energy!
set -e  # Exit immediately on any error

WHL_FILE="torch-2.9.0a0+gitc665594-cp310-cp310-linux_x86_64.whl"
RELEASE_URL="https://github.com/Yyyzk123/pytorch-cuda128-sm120/releases/download/v2.9.0-sm120/$WHL_FILE"

echo "🔍 Step 1: Checking environment..."
# Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found! Please install it from https://www.python.org/downloads/"
    exit 1
fi

# pip
if ! command -v pip &> /dev/null; then
    echo "❌ pip not found! Please install it from https://pip.pypa.io/en/stable/installation/"
    exit 1
fi

# pip upgrade
echo "🔄 Upgrading pip (recommended >= 21.0)..."
pip install --upgrade pip || echo "⚠️ pip upgrade failed, continuing..."

# NVIDIA GPU check
if command -v nvidia-smi &> /dev/null; then
    echo "✅ NVIDIA driver detected. CUDA support likely available."
else
    echo "⚠️ No NVIDIA driver found. Please install CUDA 12.8: https://developer.nvidia.com/cuda-downloads"
    echo "   Quick steps: Download → Run installer → Restart terminal"
fi

echo "📦 Step 2: Activating virtual environment..."
if command -v conda &> /dev/null; then
    echo "🔗 Using Conda environment..."
    source "$(conda info --base)/etc/profile.d/conda.sh" || {
        echo "❌ Failed to load Conda. Please check installation."
        exit 1
    }
    ENV_NAME="gs_env"
    if ! conda activate "$ENV_NAME" &> /dev/null; then
        echo "⚙️ Creating new Conda env: $ENV_NAME ..."
        conda create -n "$ENV_NAME" python=3.10 -y
        conda activate "$ENV_NAME"
    fi
    PYTHON_CMD="python"
else
    echo "🔗 Using Python venv (recommended for beginners)..."
    ENV_DIR=".venv"
    if [ ! -d "$ENV_DIR" ]; then
        echo "🛠️ Creating virtual environment..."
        python3 -m venv "$ENV_DIR" || {
            echo "❌ Failed to create venv. Make sure Python supports it."
            exit 1
        }
    fi
    source "$ENV_DIR/bin/activate" || {
        echo "❌ Failed to activate venv!"
        exit 1
    }
    PYTHON_CMD="python"
fi

echo "🚀 Step 3: Installing PyTorch..."

if [ ! -f "$WHL_FILE" ]; then
    echo "📁 $WHL_FILE not found in current directory. Trying to download..."
    wget "$RELEASE_URL" || {
        echo "❌ Failed to download! Manually visit:"
        echo "   $RELEASE_URL"
        echo "⚠️ Release might be unpublished. Stay tuned for updates: https://github.com/Yyyzk123/pytorch-cuda128-sm120"
        exit 1
    }
fi

echo "📥 Installing: $WHL_FILE ..."
pip install "$WHL_FILE" || {
    echo "❌ Installation failed! Check pip version or Python compatibility."
    exit 1
}

echo "🧪 Verifying installation and CUDA support..."
$PYTHON_CMD -c "
import torch
print('Torch version:', torch.__version__)
if torch.cuda.is_available():
    print('✅ CUDA available. GPU:', torch.cuda.get_device_name(0))
    print('CUDA version:', torch.version.cuda)
    print('✨ All systems GO! Light up your AI project!')
else:
    print('⚠️ CUDA not detected. Check NVIDIA driver or CUDA 12.8 install.')
" || {
    echo "❌ Python test failed! Something is wrong with your environment."
    exit 1
}

echo "🎉 Installation complete! Your GPU is ready to accelerate AI."

echo "🧭 Next Steps:"
printf "%-20s | %-45s\n" "Action" "Description"
echo "--------------------|---------------------------------------------------------------"
printf "%-20s | %-45s\n" "Run demo" "Try Gaussian Splatting or SplaTAM project"
printf "%-20s | %-45s\n" "Report issues" "Open an issue: https://github.com/Yyyzk123/pytorch-cuda128-sm120/issues"
printf "%-20s | %-45s\n" "Exit env" "Run deactivate (for venv) or conda deactivate"
