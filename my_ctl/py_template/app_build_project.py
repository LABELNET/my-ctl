#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
   @File    :   app_build_project.py
   @Create  :   2023/03/14 20:42:00
   @Author  :   Yuan Mingzhuo
   @Update  :   2023/03/14
   @License :   (C)Copyright 2014-2023 YuanMingZhuo All Rights Reserved 
   @Desc    :   Coding Below
"""

import os
import shutil

from os.path import join, exists


"""
./build
├── main.py
├── package.json
├── my_ctl
│   ├── app.py
│   └── __init__.py
└── static
    └── README.md
"""


def build_project_source(project_dirname, package):
    """
    模块-开发环境-源码包-Setuptools
    ---
    1）复制源码到 build 文件夹
    2）复制静态文件到 build 文件夹
    3）创建 setup.py
    """
    # 源码位置
    build = package["build"]
    dirname_source = join(project_dirname, build["src"])
    dirname_static = join(project_dirname, build["static"])
    print(dirname_static)
    # 编译位置
    dirname_build = join(project_dirname, "build")
    dirname_json = join(project_dirname, "*.json")
    # dirname_package_json = join(project_dirname, "package.json")
    dirname_main = join(project_dirname, "main.py")
    dirname_requirement = join(project_dirname, "requirements.txt")
    if not os.path.exists(dirname_main):
        LOG = "BUILD PROJECT BINARY : NOT FOUND main.py"
        print(LOG)
        return
    # 复制操作
    # cammands = [
    #     "mkdir %s" % (dirname_build),
    #     "cp -rf %s %s" % (dirname_source, dirname_build),
    #     "cp -rf %s %s" % (dirname_static, dirname_build),
    #     "cp -f %s %s" % (dirname_json, dirname_build),
    #     "cp -f %s %s" % (dirname_main, dirname_build),
    #     "cp -f %s %s" % (dirname_requirement, dirname_build),
    #     "rm -f %s/%s" % (dirname_build, "config.yaml")
    # ]
    # cmd = " && ".join(cammands)
    # os.system(cmd)
    if not exists(dirname_build):
        os.makedirs(dirname_build)
    shutil.copytree(dirname_source, dirname_build)
    shutil.copytree(dirname_static, dirname_build)
    shutil.copy(dirname_json, dirname_build)
    shutil.copy(dirname_main, dirname_build)
    shutil.copy(dirname_requirement, dirname_build)


"""
./build
├── package.json
├── my_ctl.bin
└── static
    └── README.md
"""


def build_project_binary(project_dirname, package):
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
    dirname_static = join(project_dirname, build["static"])
    dirname_main = join(project_dirname, "main.py")
    if not os.path.exists(dirname_main):
        LOG = "BUILD PROJECT BINARY : NOT FOUND main.py"
        print(LOG)
        return
    # 执行编译
    cammands = ["cd %s" % project_dirname]
    nuitka = ["python", "-m", "nuitka", "--no-pyi-file", "--nofollow-imports"]
    for root, dirs, files in os.walk(name):
        root = str(root).replace("/", ".")
        nuitka.append("--include-package=%s" % (root))
    nuitka.append("--remove-output")
    nuitka.append("--output-dir=build")
    nuitka.append("-o build/%s.bin" % (name))
    nuitka.append("main.py")
    cmd = " ".join(nuitka)
    cammands.append(cmd)
    cmd = " && ".join(cammands)
    print("BUILD PROJECT CMD:", cmd)
    os.system(cmd)
    # 复制资源
    # dirname_package_json = join(project_dirname, "package.json")
    dirname_json = join(project_dirname, "*.json")
    dirname_requirement = join(project_dirname, "requirements.txt")
    # cammands = [
    #     "cp -rf %s %s" % (dirname_static, dirname_build),
    #     "cp -f %s %s" % (dirname_json, dirname_build),
    #     "cp -f %s %s" % (dirname_requirement, dirname_build),
    #     "rm -f %s/%s" % (dirname_build, "config.yaml"),
    # ]
    # cmd = " && ".join(cammands)
    # os.system(cmd)
    shutil.copytree(dirname_static, dirname_build)
    shutil.copy(dirname_json, dirname_build)
    shutil.copy(dirname_main, dirname_build)
    shutil.copy(dirname_requirement, dirname_build)
