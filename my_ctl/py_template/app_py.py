#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
   @File    :   app_py.py
   @Create  :   2023/03/14 18:14:41
   @Author  :   Yuan Mingzhuo
   @Update  :   2023/03/14
   @License :   (C)Copyright 2014-2023 YuanMingZhuo All Rights Reserved 
   @Desc    :   Coding Below
"""

from .app_dir import new_module, new_project
from .app_dir_src import new_module_src, new_project_src
from .app_dir_static import new_static
from .app_dir_docs import new_docs
from .app_dir_test import new_tests
from .app_dir_ai import new_ai

from .app_tools import build_package_project, build_package_module,clear_cache
from .app_build_module import build_module_binary, build_module_source
from .app_build_project import build_project_binary, build_project_source


def create_python(project_name, mode):
    """ 
    工程创建，Python
    """
    if mode == 'module':
        new_module(project_name)
        new_module_src(project_name)
        new_static(project_name)
        new_docs(project_name)
        new_tests(project_name)
        return

    if mode == 'project':
        new_project(project_name)
        new_static(project_name)
        new_docs(project_name)
        new_tests(project_name)
        new_project_src(project_name)
        return

    if mode == 'model':
        new_module(project_name)
        new_static(project_name)
        new_docs(project_name)
        new_tests(project_name)
        new_ai(project_name)
        return

def build_python(mode, env, project_dirname, package):
    """
    工程编译，Python 
    """
    clear_cache(project_dirname)
    # 执行打包
    if "module" == mode and "dev" == env:
        build_module_source(project_dirname, package)
        build_package_module(project_dirname, package)
        print("BUILD MODULE SOURCE SUCCESSFUL")

    if "module" == mode and "product" == env:
        build_module_binary(project_dirname, package)
        build_package_module(project_dirname, package)
        print("BUILD MODULE BINARY SUCCESSFUL")

    if "project" == mode and "dev" == env:
        # 工程源码
        build_project_source(project_dirname, package)
        build_package_project(project_dirname, package, env)
        print("BUILD PROJECT SOURCE SUCCESSFUL")

    if "project" == mode and "product" == env:
        # 工程二进制文件
        build_project_binary(project_dirname, package)
        build_package_project(project_dirname, package, env)
        print("BUILD PROJECT BINARY SUCCESSFUL")