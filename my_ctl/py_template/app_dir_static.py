#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
   @File    :   app_dir_static.py
   @Create  :   2023/03/14 12:35:37
   @Author  :   Yuan Mingzhuo
   @Update  :   2023/03/14
   @License :   (C)Copyright 2014-2023 YuanMingZhuo All Rights Reserved 
   @Desc    :   Coding Below
"""

from os import mkdir, getcwd
from os.path import join,exists


def new_file(file_name, data):
    """
    create new file
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(data)


def new_static_dir(project_name):
    """
    root_dir/static
    """
    static_path = join(getcwd(), project_name, 'static')
    if exists(static_path):
        return
    mkdir(static_path)

def new_static_readme(project_name):
    """
    root_dir/static/README.md
    """
    content = [
        f'# {project_name} Docs',
        '\n',
        ' 文件存放文件夹',
        ' - 若是算法模型，可将数据和算法模型下载到此文件夹',
        ' - 若是容器服务，此文件夹为容器映射文件夹，做持久化使用'
    ]
    readme_file = join(getcwd(), project_name, 'static', 'README.md')
    data = '\n'.join(content)
    new_file(readme_file, data)


def new_static(project_name):
    """
    Export static
    """
    new_static_dir(project_name)
    new_static_readme(project_name)