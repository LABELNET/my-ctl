#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
   @File    :   app_build.py
   @Create  :   2023/03/14 20:41:25
   @Author  :   Yuan Mingzhuo
   @Update  :   2023/03/14
   @License :   (C)Copyright 2014-2023 YuanMingZhuo All Rights Reserved 
   @Desc    :   Coding Below
"""

from .py_template import check_configs, build_python

import click


@click.command(help="工程构建, 构建源码包和二进制包")
@click.option(
    '--env',
    '-e',
    type=click.Choice(['dev', 'product']),
    default='product',
    prompt='输入工程构建环境',
    help='构建类型, dev 构建源码包，product 构建二进制包',
)
def build(env):
    """
    工程构建， 构建源码包和二进制包
    """
    # 构建
    is_exists, package, dirname_project = check_configs()
    if not is_exists:
        return
    mode = package["mode"]
    # 构建BUILD
    build_python(mode, env, dirname_project, package)
