#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
   @File    :   app_dir_src.py
   @Create  :   2023/03/21 14:32:12
   @Author  :   Yuan Mingzhuo
   @Update  :   2023/03/21
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

def new_src_cmakelist(project_name):
    """ 
    root_dir/src/CMakeList
    """
    content = [
        'aux_source_directory(. DIR_LIB_SRCS)',
        '\n',
        '# 添加目录',
        'include_directories(../include)',
        '\n',
        'set(LIBRARY_OUTPUT_PATH ${PROJECT_BINARY_DIR}/lib)',
        '\n',
        '# 生成链接库',
        'add_library(hello ${DIR_LIB_SRCS})'
    ]
    file = join(getcwd(), project_name, 'src','CMakeLists.txt')
    data = '\n'.join(content)
    new_file(file, data)

def new_src_hello(project_name):
    """ 
    root_dir/src/hello.cc
    """
    content = [
        '#include "hello.h"',
        '\n',
        'int add(int a, int b)',
        '{',
        '    return a+b;',
        '}' 
    ]
    file = join(getcwd(), project_name, 'src','hello.cc')
    data = '\n'.join(content)
    new_file(file, data)

def new_include_hello(project_name):
    """
    root_dir/include/hello.h  
    """
    content = [
        '\n',
        'int add(int a, int b);'
    ]
    file = join(getcwd(), project_name, 'include','hello.h')
    data = '\n'.join(content)
    new_file(file, data)

def create_demo(project_name):
    """ 
    创建 Demo
    """
    new_src_cmakelist(project_name)
    new_src_hello(project_name)
    new_include_hello(project_name)

