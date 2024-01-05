#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
   @File    :   app_tools.py
   @Create  :   2023/03/14 20:41:33
   @Author  :   Yuan Mingzhuo
   @Update  :   2023/03/14
   @License :   (C)Copyright 2014-2023 YuanMingZhuo All Rights Reserved 
   @Desc    :   Coding Below
"""

from os.path import dirname, abspath, join, exists
import os
import yaml
import shutil
import tarfile

"""
命令操作函数
"""


def check_name(name):
    """
    检查-名称是否符合规范: a-b-c
    """
    if len(str(name)) == 0:
        return False
    if "-" not in name:
        return False
    return True


def placeholder_replace(file, holder, name):
    """
    项目-文件占位符替换
    """
    content = ""
    # 读
    with open(file, "r", encoding="utf-8") as f:
        content = str(f.read())
    # 替
    content = content.replace(holder, name)
    # 写
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)


def static_template_dir():
    """
    获取静态文件夹路径
    """
    root_dirname = dirname(dirname(abspath(__file__)))
    static_dirname = join(root_dirname, "static")
    return static_dirname


def get_configs(package_dir):
    """
    获取 config.yaml 文件具体 key 的值
    ---
    package_dir: yaml 配置路径
    """
    content = {}
    # 读
    with open(package_dir, "r", encoding="utf-8") as f:
        content = yaml.safe_load(f.read())
    content = content["project"]
    return content


def clear_cache(project_dirname):
    """
    清理缓存
    ---
    包括: build , __pycache__ , *.onnx , *.engine
    """
    # cammand = [
    #     "cd %s" % project_dirname,
    #     "rm -rf dist",
    #     "rm -rf build",
    #     "find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete",
    #     "find . -type f -name '*.onnx' -delete -o -type d",
    #     "find . -type f -name '*.engine' -delete -o -type d",
    # ]
    # cmd = " && ".join(cammand)
    # print("BUILD CLEAR:", cmd)
    # res = os.system(cmd)
    shutil.rmtree(join(os.getcwd(), project_dirname, "dist"), ignore_errors=True)
    shutil.rmtree(join(os.getcwd(), project_dirname, "build"), ignore_errors=True)
    # if res == 0:
    #     print("BUILD CLEAR SUCCESSFUL")
    #     return True
    # else:
    #     print("BUILD CLEAR ERROR")
    #     return False
    return True


def get_version(version, env):
    """
    版本号，约定
    ---
    is_dev = True , version = version + .1
    is_dev = False, version
    """
    if "dev" == env:
        version += ".1"
    return version


def init_setup_py(project_dirname, package, env):
    """
    初始化 setup file
    ---
    - package_dir ， 项目目录
    - 根据 package.json 生成
    """
    # 初始化 setup 文件
    setup_py_dirname = join(project_dirname, "setup.py")
    if os.path.exists(setup_py_dirname):
        os.remove(setup_py_dirname)
    # 版本
    version = get_version(package["version"], env)
    # entry_point
    entry_points = package["entry_points"]
    entry_content = ["[console_scripts]"]
    if len(entry_points.keys()) > 0:
        for key in entry_points.keys():
            script = "%s=%s" % (key, entry_points[key])
            entry_content.append(script)
    entry_content_string = "\r\n".join(entry_content)
    # 写入 setup.py
    content = [
        "from setuptools import setup, find_packages",
        "setup(",
        f"name='{package['name']}',",
        f"version='{version}',",
        f"description='{package['description']}',",
        f"author_email='{package['author_email']}',",
        f"author='{package['author']}',",
        f"license='{package['license']}',",
        f"keywords={str(package['keywords'])},",
        "packages=find_packages(),",
        "include_package_data=True,",
        f"install_requires={str(package['requirements'])},",
        "python_requires='>=3.8',",
        'entry_points="""\n%s\n"""' % (entry_content_string),
        ")",
    ]
    content = "\r\n".join(content)
    with open(setup_py_dirname, "w") as file:
        file.write(content)
    return setup_py_dirname


def init_manifest_file(project_dirname, build):
    """
    初始化 MANIFEST.in
    ---
    project_dirname , 根目录
    build , { "src":"code" , "static" : "static resource" }
    """
    manifest_file_dirname = join(project_dirname, "MANIFEST.in")
    dirname_source = build["src"]
    dirname_static = build["static"]
    content = [
        "include %s/*" % (dirname_source),
        "include %s/*/*" % (dirname_source),
        "recursive-include %s %s *" % (dirname_source, dirname_static),
    ]
    content = "\r\n".join(content)
    with open(manifest_file_dirname, "w") as file:
        file.write(content)
    return manifest_file_dirname


def init_package_file(project_dirname, source):
    """
    初始化 二进制包  __init__ 路径
    ---
    project_dirname ，根目录
    """
    package_file_dirname = join(project_dirname, "build", source, "__init__.py")
    # PATH
    package_static_path = str(source).upper() + "_STATIC"
    content = [
        "import importlib",
        "import os",
        "import sys" "\n",
        f"from .{source} import *",
        "\n# MODULE REGISTER",
        f"globals().update(importlib.import_module('{source}').__dict__)",
        "\n# STATIC PATH",
        "if sys.platform.startswith('linux'):",
        f"\tos.environ['{package_static_path}'] = os.path.dirname(os.path.abspath(__file__))",
    ]
    content = "\r\n".join(content)
    with open(package_file_dirname, "w") as file:
        file.write(content)
    return package_file_dirname


def check_configs():
    """
    检查 Package JSON
    ---
    - is exists ，是否存在
    - package.json , json 对象
    """
    project_dirname = os.getcwd()
    package_dirname = os.path.join(project_dirname, "config.yaml")

    if not os.path.exists(package_dirname):
        LOG = "ERROR: 没有找到 package.json，%s " % (package_dirname)
        print(LOG)
        return False, None, project_dirname
    # 配置文件
    package = get_configs(package_dirname)
    return True, package, project_dirname


def build_package_module(project_dirname, package):
    """
    模块打包
    """
    build_name = package["build"]
    print("BUILD", build_name["src"])
    # BUILD
    dirname_build = join(project_dirname, "build")
    # DIST
    dirname_dist = join(project_dirname, "dist")
    # DIST DIST
    dirname_dist_dist = join(dirname_dist, "dist")
    # 执行打包
    cammands = [
        f"cd {dirname_build}",
        f"python setup.py sdist --dist-dir {dirname_dist_dist}",
    ]
    cmd = " && ".join(cammands)
    res = os.system(cmd)
    shutil.move(join(dirname_build, f"{build_name['src']}.egg-info"), dirname_dist)
    if res == 0:
        print("BUILD MODULE SUCCESSFUL")
    else:
        print("BUILD MODULE ERROR")


def build_package_project(project_dirname, package, env):
    """
    工程打包
    ---
    1）创建临时文件夹 name-version
    2) 复制 Build 内容到临时文件夹
    3）执行 tar 打包程序
    4）删除临时文件夹
    """
    build_name = package["build"]
    print("BUILD", build_name["src"], env)
    # name
    name = package["name"]
    # 先创建版本文件夹
    version = get_version(package["version"], env)
    tar_pacakge_name = "%s-%s" % (name, version)
    tar_name = "%s.tar.gz" % (tar_pacakge_name)
    # 再打包，后删除
    dirname_build = join(project_dirname, "build")
    dirname_package_name = join(project_dirname, tar_pacakge_name)
    # dist : project/dist location
    dirname_dist = join(project_dirname, "dist")
    dirname_dist_tar_name = join(dirname_dist, tar_name)
    # cammand
    # cammands = [
    #     f"rm -rf {dirname_package_name}",
    #     f"rm -rf {dirname_dist}",
    #     f"mkdir {dirname_package_name}",
    #     f"cp -rf {dirname_build}/* {dirname_package_name}/",
    #     f"mkdir {dirname_dist}",
    #     f"tar -zcvf {dirname_dist_tar_name} {tar_pacakge_name}/",
    #     f"rm -rf {dirname_package_name}",
    # ]
    # cmd = " && ".join(cammands)
    # res = os.system(cmd)
    shutil.rmtree(dirname_package_name, ignore_errors=True)
    shutil.rmtree(dirname_dist, ignore_errors=True)
    if not exists(dirname_package_name):
        os.makedirs(dirname_package_name)
    shutil.copytree(dirname_build, dirname_package_name)
    if not exists(dirname_dist):
        os.makedirs(dirname_dist)
    with tarfile.open(dirname_dist_tar_name, "w:gz") as tar:
        tar.add(tar_pacakge_name, arcname=os.path.basename(tar_pacakge_name))
    shutil.rmtree(dirname_package_name, ignore_errors=True)
    # 返回构建路径
    print("BUILD PROJECT SUCCESSFUL")
