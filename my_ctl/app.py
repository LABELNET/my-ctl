#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
   @File    :   app.py
   @Create  :   2023/03/14 15:07:29
   @Author  :   Yuan Mingzhuo
   @Update  :   2023/03/14
   @License :   (C)Copyright 2014-2023 YuanMingZhuo All Rights Reserved 
   @Desc    :   Coding Below
"""


from .app_create import create
from .app_build import build

import click


@click.group()
def cli():
    """
    MyCtl ，Python 和 C++ 项目工程的 创建、编译、打包、发布
    """
    pass

# add command
cli.add_command(create)
cli.add_command(build)


if __name__ == "__main__":
    cli()
