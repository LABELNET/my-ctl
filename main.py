#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
   @File    :   main.py
   @Create  :   2021/09/07 12:00:32
   @Author  :   Yuan Mingzhuo
   @Update  :   2021/09/07
   @License :   (C)Copyright 2021-2023 LABELNET
   @Desc    :   Coding Below
"""

"""
命令测试
---
(base) smartahc@smartahc-server:~/roi-space/roi-ctl$ python main.py 
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  python-app     Init python app project
  python-pip     Init python pip project
  script-deploy  script shell deploy
  script-test    script shell test
"""

from my_ctl import cli

if __name__ == '__main__':
    cli()