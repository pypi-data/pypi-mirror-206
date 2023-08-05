#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup for RobotAtHome2
"""

import os
import sys

from setuptools import find_packages, setup

def read(rel_path):
    """ Docstring """
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    """ Docstring """
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")

try:
    with open("README.md", "r") as fh:
        LONG_DESCRIPTION = fh.read()
except Exception:
    LONG_DESCRIPTION = ''

# Platform specific code
if sys.platform.startswith('win'):
    PYTHON_REQUIRES = '<3.7'
elif sys.platform.startswith('linux'):
    PYTHON_REQUIRES = '>=3.7'

setup(
    name="robotathome",
    version=get_version("robotathome/__init__.py"),
    description="This package provides a Python Toolbox with a set of functions to assist in the management of Robot@Home2 Dataset",
    long_description = LONG_DESCRIPTION,
    long_description_content_type="text/markdown",

    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/goyoambrosio/RobotAtHome2",
    keywords=('toolbox '
              'dataset '
              'database '
              'relational model '
              'mobile robotics '
              'computer vision '
              ),

    author="G. Ambrosio-Cestero",
    author_email="gambrosio@uma.es",
    platforms=['Windows', 'Linux'],

    packages=find_packages(),

    install_requires=[
        "humanize",
        "click",
        "urllib3",
        "requests",
        "tqdm",
        "loguru",
        "pandas",
        "numpy"
    ],
    extras_require={
        'full':['matplotlib>=3', 'notebook','ipywidgets','opencv-python','opencv-contrib-python'],
        'interactive': ['matplotlib>=3', 'notebook', 'ipywidgets'],
        'cv': ['opencv-python','opencv-contrib-python']
    },
    python_requires=PYTHON_REQUIRES,

    tests_require=['unittest'],
    # These files will be located at ~/<anaconda-dir>/envs/<env-name>/[robotathome/schema|robotathome/notebooks|...]
    data_files=[
        ('robotathome/schema',
         ['rh_schema_diagram/rh_schema_brief.pdf',
          'rh_schema_diagram/rh_schema_full.pdf']
         ),
        ('robotathome/notebooks',
         ['notebooks/05-Google-colab-drive.ipynb',
          'notebooks/10-Download-and-install.ipynb',
          'notebooks/20-Before-starting-the-logging-system.ipynb',
          'notebooks/30-Getting-started-Framework-data.ipynb',
          'notebooks/40-Captured-data.ipynb',
          'notebooks/50-RGBD-observations.ipynb',
          'notebooks/60-Lsrscan-observations.ipynb',
          'notebooks/70-Scenes.ipynb',
          'notebooks/80-Characterized-observations.ipynb',
          'notebooks/90-The-config-file.ipynb',
          'notebooks/100-Iterating-over-RGBD-images.ipynb',
          'notebooks/110-Concatenating-images-from-multiple-cameras.ipynb',
          'notebooks/120-Making-a-video.ipynb',
          'notebooks/130-Processing-images-with-YOLO.ipynb',
          'notebooks/140-Loading-dataset-in-Google-Colab.ipynb',
          'notebooks/150-Segmentation-with-Detectron2.ipynb']
         )
    ],
    # sql files from robotathome package will be included in the installation package
    # located at ~/<anaconda-dir>/envs/<env-name>/lib/<python>/site-packages/robotathome
    package_data={'robotathome': ['*.sql']},

)
