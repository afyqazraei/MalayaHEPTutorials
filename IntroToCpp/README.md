# Introduction to C++

## For Students

UNDER CONSTRUCTION

## For contributors

These instructions are designed for those contributing using Linux via a Bash terminal, but if you're using Jupyter directly, then you need to find a workaround for some stuff that I didn't bother to explore yet.

1. Install [Anaconda](https://docs.anaconda.com/anaconda/install/).
2. Setup a Conda environment first and use it in there. 

You can read up more on how Conda environments work [here](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html). Basically, they're just a separate place you can mess around without interupting or corrupting your default setup.

```bash
conda create -n xeus-cling
```
Here, `xeus-cling` is the `conda env` we designated, and has a similar name to the C++ kernel we will install later. To enter the environment and to exit it, just type:
```bash
conda activate xeus-cling    # to enter the environment
conda deactivate             # to exit the environment
```
The `env` you just setup is empty, so you need to install the packages that you want to use, even when the default Conda environment has all of them.
```bash
conda install ipykernel
conda install notebook
```
3. Install `xeus-cling`, which is a Jupyter kernel for C++ based on the interpreter [cling](https://github.com/root-project/cling) and the native implementation of the Jupyter protocol [xeus](https://github.com/jupyter-xeus/xeus).

```bash
conda install -c conda-forge xeus-cling
```
4. Open a notebook, and start developing!

```bash
jupyter-notebook
```
