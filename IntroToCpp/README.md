# Introduction to C++

## For Students

UNDER CONSTRUCTION

## For contributors

These instructions are designed for those contributing using Linux via a Bash terminal, but if you're using Jupyter directly, then you need to find a workaround for some stuff that I didn't bother to explore yet.

1. Install anaconda at [Anaconda Installation Documentation](https://docs.anaconda.com/anaconda/install/)
2. To use the C++ interpreter Cling, we need to setup a Conda environment first and use it in there.

```bash
conda create -n xeus-cling
conda activate xeus-cling    # to enter the environment, to exit just type 'conda deactivate'
conda install ipykernel
conda install notebook
```
3. Install Xeus-Cling, which is a Jupyter kernel for C++ based on the interpreter Cling and the native implementation of the Jupyter protocol Xeus.

```bash
conda install -c conda-forge xeus-cling
```
4. Open a notebook, and start developing!

```bash
jupyter-notebook
```
