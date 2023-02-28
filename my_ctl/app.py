#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
   @File    :   roi_ctl.py
   @Create  :   2021/09/07 10:38:51
   @Author  :   Yuan Mingzhuo
   @Update  :   2021/09/07
   @License :   (C)Copyright 2014-2021 SmartAHC All Rights Reserved 
   @Desc    :   Coding Below
"""

"""

功能规划
---
- create  : 工程，输入 Gitlab 仓库名称
- builder : 构建，模块和工程
- deploy  : 发布，模块-发布私有仓库，工程-上传 OSS
- install : 依赖，私有仓库依赖安装
"""


from .app_create import create
from .app_build import build
import click

# 命令集合
# cli = click.CommandCollection(sources=[create, install])

@click.group()
def cli():
    """
    集成项目 脚手架工具
    """
    pass

cli.add_command(create)
cli.add_command(build)

if __name__ == "__main__":
    cli()
