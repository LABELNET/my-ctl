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

```
python main.py build -e product
cd dist
twine upload dist/*
``` 

> Input pypi Account And  Password
