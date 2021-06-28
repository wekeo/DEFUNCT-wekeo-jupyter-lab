# learn_olci
 
**learn-olci** is a collection of Python-based code 
designed to provide introductory training on the use 
of ocean colour data from the Ocean and Land Colour Instrument (OLCI) aboard the
Copernicus Sentinel-3 satellites that are operated (and marine data produced) by
EUMETSAT. This module is designed to stand-alone but also forms parts of wider 
EUMETSAT training activities.

## License
 
This code is licensed under an MIT license. 
See file LICENSE.txt for details on the usage and distribution terms.

All product names, logos, and brands are property of their respective owners. 
All company, product and service names used in this website are for 
identification purposes only.
 
## Authors
* [**Hayley Evers-King**](mailto://hayley.eversking@eumetsat.int) - *Initial work, current development, future development strategy and collaboration* [EUMETSAT](http://www.eumetsat.int)
* [**Ben Loveday**](mailto://Ben.Loveday@external.eumetsat.int) - *Initial work* - [EUMETSAT](http://www.eumetsat.int)
* [**Oliver Clements**](mailto://olcl@pml.ac.uk) - *Current development* - [PML](http://www.pml.ac.uk)
 
## Getting Started
  
The course is based on [Jupyter notebooks](https://jupyter.org/), which allow
a high-level of interactive learning, as code, text description and 
visualisation is combined in one place. If you have not worked with 
`Jupyter Notebooks` before, you can look at the module 
[Introduction to Python and Project Jupyter](./0_1_Intro_to_Python_and_Jupyter.ipynb) 
to get a short introduction to Jupyter notebooks and their benefits.

### Prerequisites
 
You will require Jupyter notebook to run this code. We recommend that you install the
latest Anaconda Python distribution for your operating system (https://www.anaconda.com/). 
Anaconda Python distributions include Jupyter Notebook. We recommend setting up an
environment as recommended below, however you may also adapt your current Python 
environment to include the dependencies listed.
 
#### Dependencies - CHECK VS yml...
cartopy,   0.18.0, LGPL-3.0,		  https://anaconda.org/conda-forge/cartopy 
descartes, 1.1.0,  BSD-3-Clause,      https://anaconda.org/conda-forge/descartes
earthpy,   0.9.2,  BSD-3-Clause,      https://anaconda.org/conda-forge/earthpy
folium,    0.11.0, MIT,               https://anaconda.org/conda-forge/folium
geopandas, 0.8.1,  BSD-3-Clause,      https://anaconda.org/conda-forge/geopandas
json,      0.1.1,  MIT,               https://anaconda.org/jmcmurray/json
jupyter,   1.0.0,  BSD-3-Clause,      https://anaconda.org/conda-forge/jupyter
netcdf4,   1.5.4,  MIT,               https://anaconda.org/conda-forge/netcdf4
owslib,    0.20.0, BSD-3-Clause,      https://anaconda.org/conda-forge/owslib
pandas,    1.1.3,  BSD-3-Clause,      https://anaconda.org/anaconda/pandas
plotly,    4.11.0, MIT,               https://pypi.org/project/plotly/
texttable, 1.6.3,  LGPL-3.0,		  https://anaconda.org/conda-forge/texttable
xmltodict, 0.12.0, MIT,               https://anaconda.org/conda-forge/xmltodict

### Setting up a Python Environment
 
This collection supports Python 3.6. Although many options are possible, the 
authors highly recommend that users install the appropriate Anaconda package 
for their operating system.

Python allows users to create specific environments that suit their applications. 
This tutorials included in this collection require a number of non-standard 
package - by which we refer to those no included by default in Anaconda. In this 
directory, users will find a *eumetsat_data_services.yaml* file which can be used 
as follows to construct a environment that will install all the required packages.

To construct the environment, please run the following command from your 
**Anaconda prompt** (or analogous, if you are not using Anaconda). You should be 
able to find/open your Anaconda prompt from your start menu (or dock, or via 
running the Anaconda Navigator).

Once the prompt is open, navigate to the **learn_olci** source 
folder (e.g. the folder where this file is). This article may be some help here, if 
you are new to the command line (https://docs.anaconda.com/ae-notebooks/user-guide/basic-tasks/apps/use-terminal/).

To create the environment, run:

**conda env create -f eumetlab_environment.yaml**

The environment won't be activated by default. To activate it, run:

**conda activate eumetsat_data_services**

*Note: remember that you may need to reactivate the environment in every 
new window instance*


### Running Jupyter Notebook

To to run Jupyter Notebook, open an Anaconda prompt and make sure you have activated 
the correct environment. Again, navigate to the **learn-olci** 
source folder. Once you are in the correct folder, run Jupyter using:

**jupyter notebook**

This should open Jupyter Notebooks in a browser window. On occasion, Jupyter may not
be able to open a window and will give you a URL to past in your browser. Please do
so, if required.

*Note: Jupyter Notebook is not able to find modules that are 'above' it in a directory 
tree, and you will unable to navigate to these. So make sure you run the line above 
from the correct directory!*