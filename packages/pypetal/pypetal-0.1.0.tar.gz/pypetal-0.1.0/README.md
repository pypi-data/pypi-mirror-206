# pyPETaL: A Pipeline for Estimating AGN Time Lags

[![Documentation Status](https://readthedocs.org/projects/pypetal/badge/?version=latest)](https://pypetal.readthedocs.io/en/latest/?badge=latest)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Workflow Status](https://img.shields.io/github/actions/workflow/status/Zstone19/pypetal/python-package.yml)](https://img.shields.io/github/actions/workflow/status/Zstone19/pypetal/python-package.yml)
[![License](https://img.shields.io/github/license/Zstone19/pypetal)](https://img.shields.io/github/license/Zstone19/pypetal)
[![codecov](https://codecov.io/gh/Zstone19/pypetal/branch/main/graph/badge.svg?token=00O40N9H05)](https://codecov.io/gh/Zstone19/pypetal)



## Installation

### pyPetal

pyPetal is available on PyPI and can be installed with pip: **(NOT IMPLEMENTED YET)**
```
    pip install pypetal
```

Or, if you want to install the latest development version:
```
    git clone https://github.com/Zstone19/pypetal.git
    cd pypetal
    pip install .
```


PLIKE is an optional algorithm that is used in pyPetal. There is a script available in the main directory to install and compile PLIKE (assuming that `gfortran` is installed). To install PLIKE, run the following command:
```
    sh build_plike.sh
```



### pyPetal and JAVELIN

The JAVELIN software used in pyPetal runs on Python 2, though the bulk of pyPetal software relies on Python >=3.8. To circumvent this issue, pyPetal has a JAVELIN "module" (``pypetal-jav``) that can be installed as a separate package and used in conjunction with pyPetal, in a Python 2 environment.


External requirements (not installed by ``pip`` or ``setup.py``):
```
    A Fortran compiler (>F90)
```


pyPetal-jav is available on PyPI and can be installed with pip:
```
    pip install pypetal-jav
```


Or, if you want to install the latest development version:
```
    git clone https://github.com/Zstone19/pypetal-jav.git
    cd pypetal-jav
    pip install .
```


__NOTE:__ The user may need to install ``NumPy`` before installing pyPetal-jav through ``pip`` or ``setup.py``. This is because ``JAVELIN`` requires ``NumPy`` in order to be installed. This can be done with:
```
    pip install numpy
```
