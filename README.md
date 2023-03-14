# my-ctl

Python 项目脚手架工具

> Python 3.8 

## Install

```
pip install my-ctl
```

## Use

```
$ myctl --help
Usage: main.py [OPTIONS] COMMAND [ARGS]...

  集成项目 脚手架工具

Options:
  --help  Show this message and exit.

Commands:
  build   项目构建, 构建源码包和二进制包
  create  项目创建, 根据模板创建集成项目工程目录结构
```

## Build & Deploy

```
python main.py build -e product
cd dist
twine upload dist/*
``` 

> Input pypi Account And  Password
