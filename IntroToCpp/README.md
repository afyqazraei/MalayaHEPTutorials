# Introduction to C++

## For Students

UNDER CONSTRUCTION

## For contributors

These instructions are designed for those contributing using Linux via a Bash terminal, but if you're using Jupyter directly, then you need to find a workaround for some stuff that I didn't bother to explore yet.

1. Install [Anaconda](https://docs.anaconda.com/anaconda/install/).
2. Setup a Conda environment first and use it in there. 

You can read up more on how Conda environments work [here](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html). Basically, they're just a separate place you can mess around without interupting or corrupting your default setup.

```bash
conda create -n root_env
```
Here, `root_env` is the `conda env` we designated, and has a similar name to the C++ kernel we will install later. To enter the environment and to exit it, just type:
```bash
conda activate root_env      # to enter the environment
conda deactivate             # to exit the environment
```
The `env` you just setup is empty, so you need to install the packages that you want to use, even when the default Conda environment has all of them.
```bash
conda install ipykernel
conda install notebook
```
3. Install ROOT, a framework widely used for the big data analyses carried out at CERN. It uses the Cling C++ interpreter and has a very large library.

```bash
conda install -c conda-forge root
```
4. Open a notebook, and start developing!

```bash
jupyter-notebook
```
