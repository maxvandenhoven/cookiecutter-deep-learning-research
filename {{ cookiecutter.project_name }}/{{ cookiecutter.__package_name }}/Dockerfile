# Use NVIDIA CUDA base image to support Pytorch with GPU. 
ARG CUDA_VERSION=11.8.0
ARG CUDNN_VERSION=8
ARG UBUNTU_VERSION=20.04
FROM nvidia/cuda:${CUDA_VERSION}-cudnn${CUDNN_VERSION}-devel-ubuntu${UBUNTU_VERSION}

# Set bash as the current shell.
RUN chsh -s /bin/bash
SHELL ["/bin/bash", "-c"]

# Set environment variables to keep tzdata install from hanging.
ENV DEBIAN_FRONTEND=noninteractive LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=Europe/Amsterdam

# Install system packages.
RUN apt-get update && apt-get install -y --allow-downgrades --allow-change-held-packages --no-install-recommends \
    build-essential bzip2 ca-certificates cmake curl docker.io ffmpeg g++ git gnuplot \
    htop ibverbs-providers libibverbs1 libjpeg-dev libpng-dev librdmacm1 libgtk2.0-dev \
    libglib2.0-0 libxext6 libsm6 libxrender1 mercurial subversion tmux unzip vim wget 

# Install Anaconda to manage Python environments.
RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.js.map' -delete && \
    /opt/conda/bin/conda clean -afy

# Add conda to PATH to make it executable.
ENV PATH /opt/conda/bin:$PATH

# Setup conda virtual environment to run the main codebase.
ARG CONDA_ENV_NAME={{ cookiecutter.__package_name }}
ARG PYTHON_VERSION=3.10.14
RUN conda update --name base --channel defaults conda && \
    conda create --name ${CONDA_ENV_NAME} ${PYTHON_VERSION:+python=${PYTHON_VERSION}} && \
    echo "conda activate ${CONDA_ENV_NAME}" >> ~/.bashrc
ENV PATH /opt/conda/envs/${CONDA_ENV_NAME}/bin:$PATH
ENV CONDA_DEFAULT_ENV ${CONDA_ENV_NAME}

# Copy all source code to working directory within the container.
ARG WORKDIR_FOLDER_CONTAINER=/workdir
WORKDIR ${WORKDIR_FOLDER_CONTAINER}

{% if cookiecutter.base_framework == "pytorch" %}
# Install PyTorch.
ARG PYTORCH_VERSION=2.0.0
ARG TORCHAUDIO_VERSION=2.0.0
ARG TORCHVISION_VERSION=0.15.0
ARG PYTORCH_CUDA_VERSION=11.8
RUN conda install --name ${CONDA_ENV_NAME} \
    pytorch${PYTORCH_VERSION:+==PYTORCH_VERSION} \
    torchvision${TORCHVISION_VERSION:+==TORCHVISION_VERSION} \
    torchaudio${TORCHAUDIO_VERSION:+==TORCHAUDIO_VERSION} \
    pytorch-cuda${PYTORCH_CUDA_VERSION:+=PYTORCH_CUDA_VERSION} --channel pytorch --channel nvidia
{% endif %}

{% if cookiecutter.setup_openmmlab == true %}
# Install OpenMMLab packages.
ARG MMCV_VERSION=2.1.0
ARG MMENGINE_VERSION=0.10.3
ARG MMDETECTION_VERSION=3.2.0
ARG MMDETECTION3D_VERSION=1.4.0
RUN pip install openmim && \
    mim install \
    "mmcv${MMCV_VERSION:+==${MMCV_VERSION}}" \
    "mmengine${MMENGINE_VERSION:+==${MMENGINE_VERSION}}" \
    "mmdet${MMDETECTION_VERSION:+==${MMDETECTION_VERSION}}" \
    "mmdet3d${MMDETECTION3D_VERSION:+==${MMDETECTION3D_VERSION}}"
{% endif %}

# Intall other Python requirements.
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Install ipykernel to run Jupyter notebooks within the container.
RUN pip install ipykernel && python -m ipykernel install --user --name ${CONDA_ENV_NAME}