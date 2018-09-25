#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Victor Calderon
# Created : 2018-09-25 
# Modified: 2018-09-25
# Vanderbilt University
from __future__ import print_function, division, absolute_import
__author__     =['Victor Calderon']
__copyright__  =["Copyright 2018 Victor Calderon, create_dirs"]
__email__      =['victor.calderon@vanderbilt.edu']
__maintainer__ =['Victor Calderon']
"""
Creates the folder structure for dotAstronomy X.
"""
# Modules
import os
import git
from pathlib import Path
from cosmo_utils.utils import work_paths as wp
from cosmo_utils.utils import file_utils  as cfutils

# Functions

def create_dirs():
    """
    Creates the folder structure for 'dotAstronomy X'
    """
    # Constants
    ndays = 4
    # Main repository
    base_dir = wp.git_root_dir()
    # Creating directories
    for day in range(1, ndays + 1):
        # Folder Structure
        day_dir          = os.path.join(base_dir, 'Day_0{0}'.format(day))
        presentation_dir = os.path.join(day_dir , 'Presentations')
        parallel_dir     = os.path.join(day_dir , 'Parallel')
        readme_1_path    = os.path.join(base_dir, 'README.md')
        readme_2_path    = os.path.join(day_dir , 'README.md')
        # Creating folders and directories
        cfutils.Path_Folder(day_dir)
        cfutils.Path_Folder(presentation_dir)
        cfutils.Path_Folder(parallel_dir)
        Path(readme_1_path).touch()
        Path(readme_2_path).touch()
        # Checking files
        cfutils.File_Exists(readme_1_path)
        cfutils.File_Exists(readme_2_path)

def main():
    """
    Creates the folder structure for 'dotAstronomy - X'
    """
    create_dirs()

if __name__ == '__main__':
    main()