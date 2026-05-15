FROM python:3.11-slim

# Install system dependencies for crawling and web tools
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /learning_lab

# Install core learning and automation packages
RUN pip install --no-cache-dir \
    torch \
    torchvision \
    torchaudio \
    jupyterlab \
    crawl4ai \
    firecrawl-py \
    pandas \
    matplotlib \
    beautifulsoup4 \
    jinja2

# Expose Jupyter and potential Web UI ports
EXPOSE 8888 8080

# Default command to keep container alive and ready for tasks
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser"]
