#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
   @File    :   app_build_module.py
   @Create  :   2023/03/14 20:42:26
   @Author  :   Yuan Mingzhuo
   @Update  :   2023/03/14
   @License :   (C)Copyright 2014-2023 YuanMingZhuo All Rights Reserved 
   @Desc    :   Coding Below
"""

import os
import shutil

from os.path import join, exists
from .app_tools import init_setup_py, init_manifest_file, init_package_file


"""
module dir
├── dist
│   ├── my_ctl-1.0.0-py3-none-any.whl
│   └── my-ctl-1.0.0.tar.gz
├── MANIFEST.in
├── my_ctl.egg-info
│   ├── dependency_links.txt
│   ├── PKG-INFO
│   ├── requires.txt
│   └── top_level.txt
├── setup.py
└── version.info
"""


def build_module_source(project_dirname, package):
    """
    模块-开发环境-源码包-Setuptools
    ---
    1）复制源码到 build 文件夹
    2）复制静态文件到 build 文件夹
    3）创建 setup.py
    4）执行 打包命令
    5）移除 源码文件夹
    """
    # 源码位置
    build = package["build"]
    package_name = build["src"]
    dirname_source = join(project_dirname, build["src"])
    dirname_static = join(project_dirname, build["static"])
    print(dirname_static)
    # 编译位置
    dirname_build = join(project_dirname, "build")
    dirname_build_build = join(dirname_build, "build")
    dirname_build_source = join(dirname_build, package_name)
    dirname_build_source_static = join(dirname_build_source, build["static"])
    # 复制操作
    # cammands = [
    #     "mkdir %s" % (dirname_build),
    #     "mkdir %s" % (dirname_build_source),
    #     "cp -rf %s %s" % (dirname_source, dirname_build_source),
    #     "cp -rf %s %s" % (dirname_static, dirname_build_source)
    # ]
    # cmd = " && ".join(cammands)
    # os.system(cmd)
    if not exists(dirname_build):
        os.makedirs(dirname_build)
    if not exists(dirname_build_source):
        os.makedirs(dirname_build_source)
    shutil.copytree(dirname_source, dirname_build_source)
    shutil.copytree(dirname_static, dirname_build_source)
    # 创建 Setup
    init_setup_py(dirname_build, package, "dev")
    init_manifest_file(dirname_build, build)
    init_package_file(project_dirname, package_name)


def build_module_binary(project_dirname, package):
    """
    模块-正式环境-二进制包-Nuitka-Setuptools
    ---
    1）执行 build 命令
    2）复制 静态文件到 build 文件夹
    3）创建 setup.py 文件
    4) 执行 打包命令
    """
    # 源码位置
    build = package["build"]
    name = build["src"]
    dirname_build = join(project_dirname, "build")
    dirname_build_source = join(dirname_build, build["src"])
    dirname_build_source_static = join(dirname_build_source, build["static"])
    dirname_static = join(project_dirname, build["static"])
    # 执行编译
    cammands = ["cd %s" % project_dirname]
    nuitka = [
        "python",
        "-m",
        "nuitka",
        "--module",
        name,
        "--no-pyi-file",
        "--nofollow-imports",
    ]
    for root, dirs, files in os.walk(name):
        if "__pycache__" in root:
            continue
        if "/" in root:
            root = str(root).replace("/", ".")
        if "\\" in root:
            root = str(root).replace("\\", ".")
        nuitka.append("--include-package=%s" % (root))
    nuitka.append("--remove-output")
    nuitka.append("--output-dir=build/%s" % (name))
    cmd = " ".join(nuitka)
    cammands.append(cmd)
    cmd = " && ".join(cammands)
    print("BUILD MODUEL CMD:", cmd)
    res = os.system(cmd)
    # 复制静态资源
    # os.system("cp -rf %s %s" % (dirname_static, dirname_build_source_static))
    if exists(dirname_static):
        shutil.copytree(dirname_static, dirname_build_source_static)
    # 初始化
    init_setup_py(dirname_build, package, "product")
    init_manifest_file(dirname_build, build)
    init_package_file(project_dirname, name)
