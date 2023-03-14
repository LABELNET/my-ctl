#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
   @File    :   app_dir_test.py
   @Create  :   2023/03/14 12:44:02
   @Author  :   Yuan Mingzhuo
   @Update  :   2023/03/14
   @License :   (C)Copyright 2014-2023 YuanMingZhuo All Rights Reserved 
   @Desc    :   Coding Below
"""

from os import mkdir, getcwd
from os.path import join, exists


def new_file(file_name, data):
    """
    create new file
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(data)


def new_tests_dir(project_name):
    """
    root_dir/tests 
    """
    test_dir = join(getcwd(), project_name, 'tests')
    if exists(test_dir):
        return
    mkdir(test_dir)


def new_test_simple(project_name):
    """
    root_dir/tests/test_simple.py  
    """
    content = [
        '\n',
        'class TestApp():',
        '    """',
        '    测试用例和文件均需要 test_xxxx 来命名',
        '    """',
        '\n',
        '    def test_two(self):',
        '        res = 2',
        '        assert  res==2',
        '\n',
        '    def test_three(self):',
        '        res = 3',
        '        assert  res!=3'
    ]
    simple_file = join(getcwd(), project_name, 'tests', 'test_simple.py')
    data = '\n'.join(content)
    new_file(simple_file, data)

def new_tests(project_name):
    """
    Export Tests
    """
    new_tests_dir(project_name)
    new_test_simple(project_name)