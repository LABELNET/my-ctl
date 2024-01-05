# my-ctl

项目工程化，脚手架工具

> Python 3.8 

## Install

```
pip install my-ctl
```

## Use

```
$ myctl --help
Usage: myctl [OPTIONS] COMMAND [ARGS]...

  MyCtl ，Python 和 C++ 项目工程的 创建、编译、打包、发布

Options:
  --help  Show this message and exit.

Commands:
  build   工程构建, 构建源码包和二进制包
  create  工程创建, 自动生成工程目录结构
```

## Build & Deploy

> pip install -r requirements.txt -i  https://pypi.tuna.tsinghua.edu.cn/simple/

```
python main.py build -e product
cd dist
twine upload dist/*
``` 

> Input pypi Account And  Password

```
username : __token__
password : pypi-AgEIcHlwaS5vcmcCJGM3MTQzMTBhLWM3NDItNDY5My1iMjQyLWY3MjdlN2QyYjYwOQACDlsxLFsibXktY3RsIl1dAAIsWzIsWyIxYTBiNzQ2Mi1kYzRiLTQzZmMtOTE3Ni1lNWU0MTQ4OWYwYjYiXV0AAAYgyLm7ptf4sKwyJ1G3Ggh_WQCOaa6c2pnn5gTbdiqV8-U
```

**.pypirc**

```
[distutils]
  index-servers =
    pypi
    PROJECT_NAME

[pypi]
  username = __token__
  password = # either a user-scoped token or a project-scoped token you want to set as the default
[PROJECT_NAME]
  repository = https://upload.pypi.org/legacy/
  username = __token__
  password = # a project token 
```