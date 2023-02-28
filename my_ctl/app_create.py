#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
   @File    :   app_create.py
   @Create  :   2021/10/28 16:37:01
   @Author  :   Yuan Mingzhuo
   @Update  :   2021/10/28
   @License :   (C)Copyright 2021-2023 LABELNET
   @Desc    :   Coding Below
"""

import os
import click
from .app_tools import (
    check_name,
    static_template_dir,
    package_json,
    readme_md,
    gitlab_config,
    docker_file,
)
from .app_middleware import cmd_middleware


def create_module(name, repository):
    """
    项目创建-模块
    """
    # 项目目录
    dir_static = static_template_dir()
    dir_template = os.path.join(dir_static, "python-pip")
    dir_module = os.path.join(os.getcwd(), name)
    if os.path.exists(dir_module):
        print("ERROR: 该路径已存在项目名称")
        return False
    # 模板复制
    package_name = str(name).replace("-", "_")
    os.mkdir(dir_module)
    # 创建模块
    cammands = [
        "cp -r %s/. %s" % (dir_template, dir_module),
        "mv %s/python_pip %s/%s" % (dir_module, dir_module, package_name),
    ]
    cmd = " && ".join(cammands)
    os.system(cmd)
    # 修改配置: package.json
    package_json(dir_module, name, repository)
    # 修改说明：README.md
    readme_md(dir_module, name)
    # 项目 GITLAB 配置
    # gitlab_config(dir_module, repository)
    return dir_module


def create_project(name, repository):
    """
    项目创建-模块
    """
    # 项目目录
    dir_static = static_template_dir()
    dir_template = os.path.join(dir_static, "python-app")
    dir_module = os.path.join(os.getcwd(), name)
    if os.path.exists(dir_module):
        print("ERROR: 该路径已存在项目名称")
        return False
    # 模板复制
    os.mkdir(dir_module)
    # 创建模块
    os.system("cp -r %s/. %s" % (dir_template, dir_module))
    # 修改配置: package.json
    package_json(dir_module, name, repository)
    # 修改说明：README.md
    readme_md(dir_module, name)
    # 修改配置：Dockerfile
    docker_image = name
    if "gitlab_image" in repository.keys():
        docker_image = repository["gitlab_image"]
    docker_file(dir_module, name, docker_image)
    # 项目 GITLAB 配置
    # gitlab_config(dir_module, repository)
    return dir_module


"""
myctl create --params

描述：项目创建，标准的项目工程目录和结构

参数: --name

- 项目名称: 格式 a-b-c，和 gitlab 仓库名称一致

参数: --mode

- 项目模式，参数必须存在
- mode = module  , 构建模块模板
- mode = project , 构建工程模板

参数：--demo 

- 有，则不检查 
- 无，则检查 
"""


@click.command(help="项目创建, 根据模板创建集成项目工程目录结构")
@click.option("--name", prompt="输入项目名称", help="项目名称, Gitlab 必须先创建项目仓库 , 约定格式 a-b-c,")
@click.option(
    "--mode",
    type=click.Choice(["module", "project"]),
    default="project",
    prompt="输入模板类型",
    help="项目类型, 支持 Module 和 Project",
)
@click.option(
    "--demo",
    type=click.Choice(["yes", "no"]),
    default="no",
    prompt="是否是示例项目",
    help="创建项目仓库",
)
def create(name, mode, demo):
    """
    项目创建，根据模板创建集成项目工程目录结构
    """
    # CHECK LOGIN
    is_pass = cmd_middleware()
    if not is_pass:
        return
    print("\n")
    print("CREATE:", "项目名称:", name, " 项目类型", mode, " 是否是示例", demo)
    # 检查名称
    if not check_name(name):
        print("CREATE:", "ERROR: 项目名称不符合规范，a-b-c")
        return
    # 检查
    repository = {}
    # 路径
    location = ""
    # 创建 Module
    if mode == "module":
        location = create_module(name, repository)
    # 创建 Project
    if mode == "project":
        location = create_project(name, repository)
    # 提醒
    print("CREATE:", "项目名称:", name, " 创建完毕: ", location)
