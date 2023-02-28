#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
   @File    :   app_tools.py
   @Create  :   2021/10/29 11:11:42
   @Author  :   Yuan Mingzhuo
   @Update  :   2021/10/29
   @License :   (C)Copyright 2021-2023 LABELNET
   @Desc    :   Coding Below
"""

from os.path import dirname, abspath, join
import os
import json

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


def placeholder_jsonequal(file, holder, holder_value):
    """
    文件-JSON 对象赋值
    """
    content = {}
    # 读
    with open(file, "r", encoding="utf-8") as f:
        content = json.loads(f.read())
    # 赋
    content[holder] = holder_value
    # 写
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(content, indent=4))


def static_template_dir():
    """
    获取静态文件夹路径
    """
    root_dirname = dirname(dirname(abspath(__file__)))
    static_dirname = join(root_dirname, "static")
    return static_dirname


def init_pacakge_json(package_dir,mode):
    """
    初始化 package json
    """
    content = {
        "name": "{NAME}",
        "mode": "module",
        "version": "1.0.0",
        "description": "Project Or Module Infomation",
        "author": "roictl",
        "author_email": "ops@smartahc.com",
        "keywords": [
            "{PACKAGE_NAME}"
        ],
        "license": "smartahc",
        "requires": [
            "requests"
        ],
        "entry_points": {},
        "python": ">=3.6",
        "repository": {},
        "environ_static": "{PACKAGE_NAME_PATH}",
        "build": {
            "source": "{PACKAGE_NAME}",
            "static": "static"
        }
    }
    if mode == "project":
        # 工程
        content["mode"] = "project"
        content["build"]["source"] = "app"
    # package json
    package_json = join(package_dir, "package.json")
    with open(package_json, "w", encoding="utf-8") as f:
        f.write(json.dumps(content, indent=4))


def package_json(package_dir, name, repository):
    """
    配置 package.json 文件
    ---
    - package_dir，项目目录
    - name，项目名称 a-b-c
    - repository，代码仓库地址
    """
    # 文件地址
    package_json = join(package_dir, "package.json")
    # {NAME}
    project_name = name
    placeholder_replace(package_json, "{NAME}", project_name)
    # {PACKAGE_NAME}
    package_name = str(name).replace("-", "_")
    placeholder_replace(package_json, "{PACKAGE_NAME}", package_name)
    # {PACKAGE_NAME_PATH}
    package_name_path = package_name.upper() + "_STATIC"
    placeholder_replace(package_json, "{PACKAGE_NAME_PATH}", package_name_path)
    # repository
    holder = "repository"
    placeholder_jsonequal(package_json, holder, repository)


def get_package_json(package_dir):
    """
    获取 package.json 文件具体 key 的值
    ---
    package_dir: package_json 路径
    """
    content = {}
    # 读
    with open(package_dir, "r", encoding="utf-8") as f:
        content = json.loads(f.read())
    return content


def readme_md(package_dir, name):
    """
    配置 readme.md 文件
    ---
    - package_dir , 项目目录
    - name , 项目名称
    """
    # 文件地址
    readme_file = join(package_dir, "README.md")
    # {NAME}
    project_name = name
    placeholder_replace(readme_file, "{NAME}", project_name)
    # {PACKAGE_NAME}
    package_name = str(name).replace("-", "_")
    placeholder_replace(readme_file, "{PACKAGE_NAME}", package_name)


def docker_file(package_dir, name, docker_image):
    """
    配置 Dockerfile
    ---
    package_dir , 项目目录
    name，项目名称
    docker_image, 镜像路径
    """
    # DOCKER FILE
    docker_file = join(package_dir, "Dockerfile")
    package_name = str(name).replace("-", "_")
    placeholder_replace(docker_file, "{PACKAGE_NAME}", package_name)
    # README
    readme_file = join(package_dir, "README.md")
    placeholder_replace(readme_file, "{DOCKER_IMAGE}", docker_image)


def gitlab_config(package_dir, repository):
    """
    配置 Gitlab 信息
    ---
    - package_dir,项目目录
    - repository, gitlba 配置信息
    """
    # 检查是否支持 git
    is_support_git = os.system("git --version")
    if is_support_git != 0:
        print("ERROR: Git 不可使用，请自行配置仓库地址")
        return
    if len(repository.keys()) == 0:
        print("ERROR: Gitlab 配置不可用，可能仓库未创建")
        return
    repo_url = repository["gitlab_url"]
    cammands = [
        "cd %s" % (package_dir),
        "git init",
        "git remote add origin %s" % (repo_url),
    ]
    cmd = " && ".join(cammands)
    os.system(cmd)


def clear_cache(project_dirname):
    """
    清理缓存
    ---
    包括: build , __pycache__ , *.onnx , *.engine
    """
    cammand = [
        "cd %s" % project_dirname,
        "rm -rf dist",
        "rm -rf build",
        "find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete",
        "find . -type f -name '*.onnx' -delete -o -type d",
        "find . -type f -name '*.engine' -delete -o -type d",
    ]
    cmd = " && ".join(cammand)
    print("BUILD CLEAR:", cmd)
    res = os.system(cmd)
    if res == 0:
        print("BUILD CLEAR SUCCESSFUL")
        return True
    else:
        print("BUILD CLEAR ERROR")
        return False


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
        "name='%s'," % (package["name"]),
        "version='%s'," % (version),
        "description='%s'," % (package["description"]),
        "author_email='%s'," % (package["author_email"]),
        "author='%s'," % (package["author"]),
        "license='%s'," % (package["license"]),
        "keywords={1},".replace("{1}", str(package["keywords"])),
        "packages=find_packages(),",
        "include_package_data=True,",
        "install_requires={2},".replace("{2}", str(package["requires"])),
        "python_requires='>=3.8',",
        "entry_points=\"\"\"\n%s\n\"\"\"" % (entry_content_string),
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
    build , { "source":"code" , "static" : "static resource" }
    """
    manifest_file_dirname = join(project_dirname, "MANIFEST.in")
    dirname_source = build["source"]
    dirname_static = build["static"]
    content = [
        "include %s/*" % (dirname_source),
        "include %s/*/*" % (dirname_source),
        "recursive-include %s %s *" % (dirname_source, dirname_static)
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
    package_file_dirname = join(
        project_dirname, "build", source, "__init__.py")
    # PATH
    package_static_path = str(source).upper()+"_STATIC"
    content = [
        "import importlib",
        "import os",
        "import sys"
        "\n",
        "from .%s import *" % (source),
        "\n# MODULE REGISTER",
        "globals().update(importlib.import_module('%s').__dict__)" % (source),
        "\n# STATIC PATH",
        "if sys.platform.startswith('linux'):",
        "\tos.environ['%s'] = os.path.dirname(os.path.abspath(__file__))" % (
            package_static_path)
    ]
    content = "\r\n".join(content)
    with open(package_file_dirname, "w") as file:
        file.write(content)
    return package_file_dirname


def check_package_json():
    """
    检查 Package JSON
    ---
    - is exists ，是否存在
    - package.json , json 对象
    """
    project_dirname = os.getcwd()
    package_dirname = os.path.join(project_dirname, "package.json")
    if not os.path.exists(package_dirname):
        LOG = "ERROR: 没有找到 package.json，%s " % (package_dirname)
        print(LOG)
        return False, None, project_dirname
    # 配置文件
    package = get_package_json(package_dirname)
    return True, package, project_dirname


def build_package_module(project_dirname, package):
    """
    模块打包
    """
    build_name = package["build"]
    print("BUILD", build_name["source"])
    # BUILD
    dirname_build = join(project_dirname, "build")
    # DIST
    dirname_dist = join(project_dirname, "dist")
    # DIST DIST
    dirname_dist_dist = join(dirname_dist, "dist")
    # 执行打包
    cammands = [
        "cd %s" % dirname_build,
        "python setup.py sdist --dist-dir %s" % (dirname_dist_dist),
        "mv %s.egg-info %s" % (build_name["source"], dirname_dist)
    ]
    cmd = " && ".join(cammands)
    res = os.system(cmd)
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
    print("BUILD", build_name["source"], env)
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
    cammands = [
        "rm -rf %s" % (dirname_package_name),
        "rm -rf %s" % (dirname_dist),
        "mkdir %s" % (dirname_package_name),
        "cp -rf %s/* %s/" % (dirname_build, dirname_package_name),
        "mkdir %s" % (dirname_dist),
        "tar -zcvf %s %s/" % (dirname_dist_tar_name, tar_pacakge_name),
        "rm -rf %s" % (dirname_package_name)
    ]
    cmd = " && ".join(cammands)
    res = os.system(cmd)
    # 返回构建路径
    if res == 0:
        print("BUILD PROJECT SUCCESSFUL")
    else:
        print("BUILD PROJECT ERROR")

