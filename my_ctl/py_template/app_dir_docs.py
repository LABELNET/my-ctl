#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
   @File    :   app_dir_docs.py
   @Create  :   2023/03/14 12:28:21
   @Author  :   Yuan Mingzhuo
   @Update  :   2023/03/14
   @License :   (C)Copyright 2014-2023 YuanMingZhuo All Rights Reserved 
   @Desc    :   Coding Below
"""

from os import mkdir, getcwd
from os.path import join, exists


def new_file(file_name, data):
    """
    create new file
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(data)


def new_docs_dir(project_name):
    """
    root_dir/docs 
    """
    docs_path = join(getcwd(), project_name, 'docs')
    if exists(docs_path):
        return
    mkdir(docs_path)


def new_docs_readme(project_name):
    """
    root_dir/docs/README.md
    """
    content = [
        f'# {project_name} Docs',
        '\n',
        ' project docs desc'
    ]
    readme_file = join(getcwd(), project_name, 'docs', 'README.md')
    data = '\n'.join(content)
    new_file(readme_file, data)


def new_docs(project_name):
    """
    Export new_docs 
    """
    new_docs_dir(project_name)
    new_docs_readme(project_name)
