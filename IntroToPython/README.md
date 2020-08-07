# Introduction to Python

<img src="https://github.com/afyqazraei/MalayaHEPTutorials/blob/master/IntroToPython/images/python-logo.png">

## For Students

Hi, everyone!

For those of you who are new to all this, welcome to GitHub! GitHub is a place where people, sometimes from all corners of the world, come together and collaborate on programming projects. Here in this repository, are Jupyter Notebooks that can be launched through Binder. All of this is open source, and can be accessible almost anywhere, anytime. 

### Jupyter Notebooks

The Notebooks will give you a brief tutorial into Python, designed for physics undergrads that have little to no experience in programming. These notebooks are adapated from previous ones made in Python, available at [IntroToPythonPERFUM](https://github.com/afyqazraei/IntroToPythonPERFUM). Just press the Binder link and let it launch. Learn, enjoy, explore!

|Notebook|Open|Contributor|
|:--|:--|:--|
|Intro To Python|N/A|Afiq Azraei|
|OOP 1: Struct and Class |N/A|Afiq Azraei|
|OOP 2: Encapsulation, Inheritance and Overloading |N/A|Afiq Azraei|
|Exploring Numpy & Scipy|N/A|N/A|
|Exploring Pandas|N/A|N/A|
|Exploring Matplotlib|N/A|N/A|

### For Advanced Students

Running on Binder requires a good internet connection, but even then it does not guarantee that the kernel would not suddenly die. So, to minimize external factors disrupting your experience to learn, it is better for you to run the ROOTbooks locally on your computer. Follow the steps outlined for contributors, then launch the notebooks from the Conda environment.


## For contributors

These instructions are designed for those contributing using Linux via a Bash terminal, but if you're using Jupyter directly, then you need to find a workaround for some stuff that I didn't bother to explore yet.

1. Install [Anaconda](https://docs.anaconda.com/anaconda/install/).
2. Setup a Conda environment first and use it in there. 

You can read up more on how Conda environments work [here](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html). Basically, they're just a separate place you can mess around without interupting or corrupting your default setup.

```bash
conda create -n myEnv
```
Here, `root_env` is the `conda env` we designated, and has a similar name to the C++ kernel we will install later. To enter the environment and to exit it, just type:
```bash
conda activate myEnv         # to enter the environment
conda deactivate             # to exit the environment
```
The `env` you just setup is empty, so you need to install the packages that you want to use, even when the default Conda environment has all of them.
```bash
conda install ipykernel
conda install notebook
```
3. The Jupyter Notebooks are designed for Python, so you should have no problems. Some libraries may not be available beforehand, so you should download them, such as Matplotlib.
```bash
conda install -c conda-forge matplotlib
```
4. Open a notebook, and start developing!

```bash
jupyter-notebook
```
