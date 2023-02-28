#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
   @File    :   app_build.py
   @Create  :   2021/10/28 16:04:22
   @Author  :   Yuan Mingzhuo
   @Update  :   2021/10/28
   @License :   (C)Copyright 2021-2023 LABELNET
   @Desc    :   Coding Below
"""

import os
import click
from .app_tools import (
    check_package_json,
    clear_cache,
    build_package_project,
    build_package_module
)
from .app_build_module import (
    build_module_binary,
    build_module_source
)
from .app_build_project import (
    build_project_binary,
    build_project_source
)
from .app_middleware import cmd_middleware

def build_execute(mode, env, project_dirname, package):
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


"""
myctl build --name  --mode  --env

描述：项目构建，生成 build 文件夹和 可发布版本压缩包

参数: --env
- 构建模式
- env = dev , 构建 源码包
- env = product , 构建 二进制包，默认二进制包
"""


@click.command(help="项目构建, 构建源码包和二进制包")
@click.option(
    "--env",
    type=click.Choice(["dev", "product"]),
    default="product",
    prompt="输入项目构建环境",
    help="构建类型, dev 构建源码包，product 构建二进制包",
)
def build(env):
    """
    项目构建， 构建源码包和二进制包
    """
    # CHECK
    is_pass = cmd_middleware()
    if not is_pass:
        return
    # 构建
    is_exists, package, dirname_project = check_package_json()
    if not is_exists:
        return
    mode = package["mode"]
    # 清理缓存
    clear_cache(dirname_project)
    # 构建BUILD
    build_execute(mode, env, dirname_project, package)
