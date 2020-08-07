# MalayaHEPTutorials

This repository will help get you started on the stuff you will be doing throughout your studies and work with University of Malaya HEP Group. Though, if you are interested to just explore around to do some programming or learn how particle physics analyses work, then you are most welcomed. 

Below, we list some tutorials scattered and available all over the Internet as a beginner reference for you. Some exercises will also be included along, primarily gearing towards work within the HEP group which mainly uses ROOT.

## UNIX

You will be mainly using the UNIX operating system on the Bash shell to access the computing grids, and this can be done in many ways. Seems like a lot of big, fancy words? Don't worry, you'll pick it up fast. First, you need to have Linux but you don't necessarily need to use dual booting. 

* If you're on Windows 10, you can use the built in Linux subsystem. Windows Subsystem for Linux 2 (WSL2) suffices our needs. Follow the the steps in this video: [How to Run Linux/Bash on Windows 10 Using the Built-In Windows Subsystem for Linux](https://www.youtube.com/watch?v=xzgwDbe7foQ)
* If you want to use a virtual machine to run Linux, follow the steps here: [How to Use VirtualBox (Beginners Guide)](https://www.youtube.com/watch?v=sB_5fqiysi4)
* If you just want to access the Grid without the hassle of installing Linux, you can just install Putty. Follow the steps here: [How to Install PuTTY on Windows](https://www.ssh.com/ssh/putty/windows/install)
* A 1-hour tutorial on the basic and useful command lines when using the Bash terminal: [Beginner's Guide to the Bash Terminal
](https://www.youtube.com/watch?v=oxuRxtrO2Ag)

### SSH (Secure Shell)

Doing proper experimental particle physics requires vast computing resources that is not possible with your own computer alone, so we will be doing it with the CMS computers. Once you have your CERN account, you can access them through the Bash shell using the `<ssh>` command. Example:

```Python
ssh -XY yourusername@lxplus7.cern.ch
>Warning: Permanently added the ECDSA host key for IP address 'IP-ADDRESS NUMBER' to the list of known hosts.
>Password:
```

If you are using Putty, then follow the steps in the previously given link.

## GitHub 

Most of the time, you will be working with lots of other people on the same code. This can be problematic if the workflow is not streamlined and may cause issues later on. So, we use Git as our version control system to ensure new entries or edits of codes are integrated properly so that the whole framework does not crash.

* A simplistic overview on how Git/GitHub works: [What is GitHub?](https://www.youtube.com/watch?v=w3jLJU7DT5E)
* A simple explanation on Version Control System: [What is Git - A Quick Introduction to the Git Version Control System](https://www.youtube.com/watch?v=OqmSzXDrJBk)
* 30-minute video tutorial on Git command lines that are useful: [Git Tutorial for Beginners: Command-Line Fundamentals](https://www.youtube.com/watch?v=HVsySz-h9r4&t=1290s)

## Python

One of the most widely used language now, Python is a common language among physicists besides C++.

* University of Malaya Physics Society (PERFUM) has an introductory course into Python available: [Introduction to Python](https://github.com/afyqazraei/IntroToPythonPERFUM)
* An in-depth tutorial for Python: [Python Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU)
* CMS Summer School also has introductory Python notebooks: [Analyse CMS Open Data in Jupyter Notebooks using Binder](https://github.com/cms-opendata-education/cms-online-notebooks-for-binder)

A set of notebooks have also been designed for this repository, mainly an adaptation of the C++ version.

## C++

C++ is the main programming language in particle physics, due to its power. Master this, as it will be useful to explore ROOT later.

A set of tutorials covering from the basics up to the concepts of Object Oriented Programming has been designed in this repo. Follow the instructions given.

* A playlist of C++ tutorials I personally find helpful: [C++ Programming Tutorials](https://www.youtube.com/playlist?list=PLAE85DE8440AA6B83)

## ROOT

ROOT is a vast statistical analysis framework designed for High Energy Physics analyses. This will be the stuff that you will commonly use and work with.

Follow the set of tutorials that have been designed to teach you the important and most used stuff, as there is A LOT if you want to explore it one by one. The tutorials will help you get started with the basics do an analysis.
* The developers have already created a set of useful tutorials for people to explore: [ROOT Tutorials](https://root.cern/doc/master/group__Tutorials.html)

