#!/bin/bash
#chmod +x install_texlive.sh
#./install_texlive.sh
set -e  # Exit on any error

# Update and install prerequisites
sudo apt update
sudo apt install -y wget perl xz-utils

# Download and extract TeX Live installer
wget https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
tar -xvzf install-tl-unx.tar.gz
cd install-tl-*

# Install TeX Live 2024 (non-interactive full install)
#sudo perl install-tl --no-interaction
sudo perl install-tl --no-interaction --scheme=full

# Set up PATH for current session (so pdflatex works right away)
export PATH=/usr/local/texlive/2024/bin/x86_64-linux:$PATH

# Also append it to ~/.bashrc for future sessions
echo 'export PATH=/usr/local/texlive/2024/bin/x86_64-linux:$PATH' >> ~/.bashrc

# Confirm install
pdflatex --version

# Clean up
cd ..
rm -rf install-tl-* install-tl-unx.tar.gz
