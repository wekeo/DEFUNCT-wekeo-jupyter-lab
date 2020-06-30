# WELCOME TO OCEAN TUTORIALS
---------------------------------------------------------------------------

**Ocean-tutorials** is a collection of Python-based code tutorials and simple tools designed to help both 
new and advanced users to work with satellite data, provided by EUMETSAT as part of the Copernicus programme,
for ocean applications. 

The content is based on [Jupyter notebooks](https://jupyter.org/), which allow
a high-level of interactive learning, as code, text description and 
visualisation is combined in one place. If you have not worked with 
`Jupyter Notebooks` before, you can look at the [Introduction to Python and Project Jupyter](./0_1_Intro_to_Python_and_Jupyter.ipynb) to get a short introduction to Jupyter notebooks and their benefits.

## Where to find what you need
The content of this repository is suitable for those completely new to Python and Copernicus marine data. You will find a range of tutorials, as well as 
some more advanced tools provided in submodules.

Below is a summary of the files provided, with recommendations on where to start:

* [Welcome to Ocean Tutorials](./Welcome_to_Ocean_tutorials.ipynb) provides an overview of the repository and further recommendations on which notebooks and
tools to look at for different applications and different backgrounds. This is the best place to start! 

*[Introduction to Python and Jupyter](./Intro_to_Python_and_Jupyter.ipynb) provides some additional background on Python and Jupyter notebooks. You might find this notebook helpful if you haven't used these tools before.

Within this repository are a number of folders that group some tutorials together thematically.

* [Sentinel-3 General Tools](./sentinel3_general_tool) contains tutorials and tools to explain fundamental aspects of Sentinel-3 data including
the file naming convention and product dissemination units. If you've never worked with the data before these tutorials will help you understand
how to identify the data you need.
* [OLCI](./OLCI) contains scripts that are primarily designed to help you learn about data provided by the Ocean Land Colour Imager (OLCI) aboard the Sentinel-3
satellites. 
* [SLSTR](./SLSTR) contains scripts that are primarily designed to help you learn about data provided by the Ocean Land Colour Imager (OLCI) aboard the Sentinel-3
satellites. 
* [SRAL](./SRAL) contains scripts that are primarily designed to help you learn about data provided by the Ocean Land Colour Imager (OLCI) aboard the Sentinel-3
satellites. 


## How to use this material

### Recommended python set up

This repository supports Python 3.7. We highly recommend that users working on their own systems 
install the appropriate Anaconda distribution for their operating system.
Here is a link to the [Anaconda distribution of Python 3.7](https://www.anaconda.com/products/individual).

### Python environments

Python allows users to create specific environments that suit their applications. 
This tutorials included in this collection require a number of non-standard 
packages - by which we refer to those no included by default in Anaconda. In this 
directory, users will find a *training.yaml* file which can be used 
as follows to construct an environment with all the required packages installed. You
can open this file in a text editor to see the packages that are used across the various scripts
in this repository.

To construct the environment, please run the following command from your 
**Anaconda prompt** (or analogous, if you are not using Anaconda). You should be 
able to find/open your Anaconda prompt from your start menu (or dock, or via 
running the Anaconda Navigator).

Once the prompt is open, navigate to the **ocean-tutorials** source 
folder (e.g. the folder where this file is). This article may be some help here, if 
you are new to the command line (https://docs.anaconda.com/ae-notebooks/user-guide/basic-tasks/apps/use-terminal/).

To create the environment, run:

**conda env create -f training.yaml**

The environment won't be activated by default. To activate it, run:

**conda activate training**

*Note: remember that you may need to reactivate the environment in every 
new window instance*

### Running Jupyter Notebook

To to run Jupyter Notebook, open an Anaconda prompt and make sure you have activated 
the correct environment. Again, navigate to the **ocean-tutorials** 
source folder. Once you are in the correct folder, run Jupyter by typing **jupyter notebook** in to the prompt.

This should open Jupyter Notebooks in a browser window. On occasion, Jupyter may not
be able to open a window and will give you a URL to past in your browser. Please do
so, if required.

*Note: Jupyter Notebook is not able to find modules that are 'above' it in a directory 
tree, and you will unable to navigate to these. So make sure you run the line above 
from the correct directory!*
