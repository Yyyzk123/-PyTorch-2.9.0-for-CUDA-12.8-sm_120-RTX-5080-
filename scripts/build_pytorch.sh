#!/usr/bin/env bash

# Build PyTorch with CUDA 12.8 and sm_120 (RTX 5080) support
set -e
set -x

export USE_CUDA=1
export USE_NINJA=1
export CMAKE_BUILD_PARALLEL_LEVEL=8
export MAX_JOBS=8
export TORCH_CUDA_ARCH_LIST="12.0"
export CUDA_HOME=/usr/local/cuda-12.8
export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$CUDA_HOME/extras/CUPTI/lib64:$LD_LIBRARY_PATH
export USE_KINETO=0

cd "$(dirname "$0")/.."

# Optional cleanup
rm -rf build dist torch.egg-info

# Install and build wheel
python setup.py install
python setup.py bdist_wheel

# Output wheel path
ls -lh dist/*.whl
