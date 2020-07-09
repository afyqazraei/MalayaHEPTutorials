# Introduction to C++

<img src="https://github.com/afyqazraei/MalayaHEPTutorials/blob/master/IntroToCpp/images/Cpp_logo.png" width="100" height="100">

## For Students

Hi, everyone!

For those of you who are new to all this, welcome to GitHub! GitHub is a place where people, sometimes from all corners of the world, come together and collaborate on programming projects. Here in this repository, are Jupyter Notebooks that can be launched through Binder. All of this is open source, and can be accessible almost anywhere, anytime. 

### Jupyter Notebooks

The Notebooks will give you a brief tutorial into c++, designed for physics undergrads that have little to no experience in programming. These notebooks are adapated from previous ones made in Python, available at [IntroToPythonPERFUM](https://github.com/afyqazraei/IntroToPythonPERFUM). Just press the Binder link and let it launch. Learn, enjoy, explore!

|Notebook|Open|Contributor|
|:--|:--|:--|
|Intro To C++|[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/afyqazraei/MalayaHEPTutorials/master?filepath=.%2FIntroToCpp%2FIntro_to_Cpp.ipynb)|Afiq Azraei|
|Basketball Shot Kinematics|N/A|Zaim Hakimie|
|Random Walk|N/A|Harith Zulfaizal|
|Simple Harmonic Motion|N/A|Yao Feng|



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
