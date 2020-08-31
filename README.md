# Welcome to WEkEO Jupyter Lab

**wekeo-jupyter-lab** is a repository of Python based tools to introduce you to the WEkEO DIAS (Data Information
and Access System) and its Jupyter Lab. The content includes notebooks explaining WEkEO and the Jupyter Lab environment and
how to use the Harmonised Data Access (HDA) that is fundamental to WEkEO. Within the submodules of this repository are 
tutorials and case studies, using data from the Copernicus Programme that are available on WEkEO and written by expert trainers
from Mercator Ocean International, ECMWF and EUMETSAT.

The content provided is mostly based on [Jupyter Notebooks](https://jupyter.org/), which allow
a high-level of interactive learning, as code, text description and visualisation 
is combined in one place. The first notebooks recommended below will give you and idea of some 
of the features that the Jupyter Notebook environment offers. 

## Copernicus Data
The notebooks contained within the repository feature the following data, all of which can be accessed through the
WEkEO HDA:
* Sentinel-3 Level 2 Ocean Colour, Sea Surface Temperature, and Altimetry
* Copernicus Marine Service products


## Where to find what you need
The content of this repository is suitable for those completely new to WEkEO, Python, Copernicus data
and hosted processing environments through to more advanced users. Further links are provided 
in the various notebooks that will allow you to access further material and examples should you wish. 

Below is a summary of the files provided, with recommendations on where to start:

* [Welcome to WEkEO Jupyter Lab](./Welcome_to_WEkEO_JupyterLab.ipynb) provides an overview of the WEkEO and it's Jupyter Lab environment. It will give you the basics on how to use the code provided for you, where to find more, and how to customise the environment to your needs. A great place to start! 

* [WEkEO Harmonized Data Access API](./wekeo-hda/WEkEO_harmonized_data_access_api.ipynb) explains how to access data on WEkEO and
makes use of functions defined in the [HDA API functions notebook](./wekeo-hda/hda_api_functions.ipynb). You will find both of these scripts in the wekeo-hda submodule provided with this repository. You will find these functions used in other notebooks, and you can use them in any you might write too! This is a great second step to take in understandinging how you can use WEkEO.

After this, you can look at some of the thematic submodules provided here:

* [WEkEO] Harmonised Data Acces (./wekeo-hda) - learn how to access data using WEkEO's data access API
* [Ocean] (./ocean) - learn about marine data from Sentinel-3 and the Copernicus Marine Service and how it can be used for different applications.

## How to use this material

If you are on GitHub/Lab you can visit 
www.wekeo.eu, register for an account and enter the JupyterLab - then follow the instructions below. 

If you are currently on the WEkEO JupyterLab you're already in the right place and can start. To clone this repository in to the WEkEO JupyterLab environment open a terminal in the WEkEO JupyterLab, type << cd public >> followed by << bash wekeo-git-clone.sh https://github.com/wekeo/wekeo-jupyter-lab.git >> This will create a clone of this repository of notebooks in your home directory. You can use the same shell script to clone any external repository you like.

You can also use this code on your own computer/Jupyter Lab server, however you won't have the fast access provided by the HDA when within the WEkEO infrastructure.


### Recommended python set up

This repository supports Python 3.7. We highly recommend that users working on their own systems install the appropriate Anaconda distribution for their operating system. Here is a link to the [Anaconda distribution of Python 3.7](https://www.anaconda.com/products/individual).

### Python environments

Python allows users to create specific environments that suit their applications. 
This tutorials included in this collection require a number of non-standard 
packages - by which we refer to those no included by default in Anaconda. These are included in the JupyterLab environment but you may need to install them for local working.




