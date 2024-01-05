#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
   @File    :   app_create.py
   @Create  :   2023/03/14 15:15:05
   @Author  :   Yuan Mingzhuo
   @Update  :   2023/03/14
   @License :   (C)Copyright 2014-2023 YuanMingZhuo All Rights Reserved 
   @Desc    :   Coding Below
"""

from .py_template import check_name, create_python
from .cc_template import create_cpp

import click


@click.command(help="工程创建, 自动生成工程目录结构")
@click.option("--name", "-n", prompt="输入工程名称", help="工程名称，名称约定格式 a-b-c")
@click.option(
    "--language",
    "-l",
    type=click.Choice(["Python", "C++"]),
    default="Python",
    prompt="输入工程语言类型",
    help="语言类型，支持 Python 和 C++",
)
@click.option(
    "--mode",
    "-m",
    type=click.Choice(["module", "project", "model"]),
    default="project",
    prompt="输入工程模板类型",
    help="工程类型, 支持 Module、Project、AI model",
)
def create(name, mode, language):
    """
    工程创建，名称 a-b-c 格式，自动生成工程目录结构
    """
    print("\n")
    # 检查名称
    if not check_name(name):
        print("ERROR:", "项目名称不符合规范，约定格式 a-b-c")
        return
    if language == "Python":
        create_python(name, mode)
    if language == "C++":
        create_cpp(name)
    print(f"Create {name} successful!")
