#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
   @File    :   app_dir.py
   @Create  :   2023/03/21 14:12:44
   @Author  :   Yuan Mingzhuo
   @Update  :   2023/03/21
   @License :   (C)Copyright 2014-2023 YuanMingZhuo All Rights Reserved 
   @Desc    :   Coding Below
"""


from os import mkdir, getcwd
from os.path import join, exists
from .app_dir_src import create_demo


def new_file(file_name, data):
    """
    create new file
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(data)


def new_gitkeep(file_dir, data):
    """
    create .gitkeep file
    """
    file_name = f'{file_dir}/.gitkeep'
    new_file(file_name, data)


def new_dir(project_name, dir_name, data):
    """
    root_dir/tests 
    """
    dir_name = join(getcwd(), project_name, dir_name)
    if exists(dir_name):
        return
    mkdir(dir_name)
    new_gitkeep(dir_name, data)


def create_dir(project_name):
    # 创建根文件夹
    root_dir = join(getcwd(), project_name)
    if exists(root_dir):
        return
    mkdir(root_dir)
    # 创建子文件夹
    dir_names = {
        '3rdparty': '第三方模块引入',
        'cmake': '多模块 cmake 文件',
        'docs': '说明文档',
        'include': '开发头文件',
        'platforms': '交叉编译平台库',
        'samples': '演示 Demo',
        'src': '源码',
        'tests': '单元测试'
    }
    for key in dir_names.keys():
        new_dir(project_name, key, dir_names[key])

def new_readme(project_name):
    """
    root_dir/README.md 
    """
    content = [
        f'# {project_name}',
        '\n Please edit project infos \n',
        '## Build',
        '\n create build dir , try `cmake ..` and `make -j` \n',
        '## Use',
        '\n use desc , try run `./demo` \n',
        '## FQA',
        '\n QA desc \n'
    ]
    readme_file = join(getcwd(), project_name, 'README.md')
    data = '\n'.join(content)
    new_file(readme_file, data)

def new_gitignore(project_name):
    """ 
    root_dir/.gitignore
    """
    content = [
        'build',
        '.vscode',
    ]
    file = join(getcwd(), project_name, '.gitignore')
    data = '\n'.join(content)
    new_file(file, data)

def new_main(project_name):
    """
    root_dir/main.cc 
    """
    content = [
        '#include <iostream>',
        '#include "hello.h"',
        '\n',
        'int main(){',
        '    std::cout << "es" <<  std::endl;',
        '    int a = add(2,33);',
        '    std::cout << a <<  std::endl;',
        '    return 0;',
        '}'
    ]
    file = join(getcwd(), project_name, 'main.cc')
    data = '\n'.join(content)
    new_file(file, data)

def new_cmakelist(project_name):
    """
    root_dir/CMakeList.txt 
    """
    content =  [
        'cmake_minimum_required(VERSION 3.18.2)',
        '\n',
        'project(demo)',
        'set(CMAKE_CXX_STANDARD 14)',
        '\n',
        'aux_source_directory(. DIR_SRCS)',
        'set(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR})',
        'add_subdirectory(src)',
        '\n',
        'add_executable(demo main.cc)',
        '\n',
        'include_directories(include)',
        '\n',
        'target_link_libraries(demo hello)'
    ]
    file = join(getcwd(), project_name, 'CMakeLists.txt')
    data = '\n'.join(content)
    new_file(file, data)

def create_project(project_name):
    """
    create root dir  
    """
    create_dir(project_name)
    new_readme(project_name)
    new_gitignore(project_name)
    new_main(project_name)
    new_cmakelist(project_name)


def create_cc(project_name):
    """
    创建C++模板工程
    """
    create_project(project_name)
    create_demo(project_name)
