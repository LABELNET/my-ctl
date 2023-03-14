#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
   @File    :   app_dir_src.py
   @Create  :   2023/03/14 11:35:26
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


def get_src_dir(project_name, mode='project'):
    """ 
    root_dir/src_dir
    """
    if mode == 'project':
        return join(getcwd(), project_name, 'app')
    module_dir = str(project_name).replace('-', '_')
    return join(getcwd(), project_name, module_dir)


def new_src_dir(project_name, mode='project'):
    """
    root_dir/src_dir 
    """
    src_dir = 'app'
    if mode == 'module':
        src_dir = str(project_name).replace('-', '_')
    src_path = join(getcwd(), project_name, src_dir)
    if exists(src_path):
        return
    mkdir(src_path)


def new_src_config(project_name, mode='project'):
    """ 
    root_dir/src/app_config.py
    """
    content = [
        'import os',
        'import yaml',
        '\n',
        'class AppConfig():',
        '    def __init__(self):',
        '        self.DEBUG = True',
        '        # custom environ data config.yaml',
        '        self.PROJECT_NAME = None',
        '\n',
        '    def create():',
        '        env = "debug"',
        '        if "ENV" in os.environ:',
        '            env = os.environ["ENV"]',
        "        if env not in ['debug', 'product']:",
        "            raise Exception(f'{env} not config')",
        '        # configs',
        "        configs = {}",
        '        with open("config.yaml", "r") as file:',
        '            configs = yaml.safe_load(file.read())',
        '        # environments',
        "        environments = configs['environments']",
        '        runtime = environments[env]',
        '        # environs',
        '        if "DEBUG" in os.environ:',
        '            runtime["DEBUG"] = os.environ["DEBUG"]',
        '        if "PROJECT_NAME" in os.environ:',
        "            runtime['PROJECT_NAME'] = os.environ['PROJECT_NAME']",
        '        # init',
        '        prod = AppConfig()',
        '        prod.__dict__ = runtime',
        '        return prod',
        '\n',
        '# exports product',
        'config = AppConfig.create()',
    ]
    src_dir = get_src_dir(project_name, mode)
    config_file = join(src_dir, 'app_config.py')
    data = '\n'.join(content)
    new_file(config_file, data)


def new_src_static(project_name, mode='project'):
    """ 
    root_dir/src/app_static.py
    """
    content = [
        'from os.path import dirname, abspath, join, exists',
        '\n',
        'import os',
        'import datetime',
        '\n',
        'def get_static():',
        '    dirname_root = dirname(dirname(abspath(__file__)))',
        '    return join(dirname_root, "static")',
        '\n',
        'def get_logger_file():',
        '    # static/logs/',
        '    dir_static = get_static()',
        '    dir_logger = join(dir_static, "logs")',
        '    if not exists(dir_logger):',
        '        os.makedirs(dir_logger)',
        '    logger_file_name = str(datetime.date.today()).replace("-", "")',
        '    logger_file = join(dir_logger, f"{logger_file_name}.log")',
        '    return logger_file'
    ]
    src_dir = get_src_dir(project_name, mode)
    static_file = join(src_dir, 'app_static.py')
    data = '\n'.join(content)
    new_file(static_file, data)


def new_src_logger(project_name, mode='project'):
    """  
    root_dir/src/app_logger.py
    """
    content = [
        'from .app_static import get_logger_file',
        'import logging',
        '\n',
        'DATE_FORMAT = "%Y-%m-%d %H:%M:%S"',
        "BASIC_FORMAT = '[%(asctime)s][%(threadName)s][%(levelname)s][ %(filename)s:%(lineno)s] : %(message)s '",
        'LOG_FORMAT = logging.Formatter(BASIC_FORMAT, DATE_FORMAT)',
        'LOG_FILE = get_logger_file()',
        'LOG_CONSOLE_HANDLER = logging.StreamHandler()',
        "LOG_FILE_HANDLER = logging.FileHandler(LOG_FILE, 'a', encoding='utf-8')",
        '\n',
        'class AppLogger():',
        '    def __init__(self):',
        "        self.logger = logging.getLogger('APP')",
        '        LOG_FILE_HANDLER.setFormatter(LOG_FORMAT)',
        '        LOG_FILE_HANDLER.setLevel(logging.INFO)',
        '        self.logger.removeHandler(LOG_FILE_HANDLER)',
        '        self.logger.addHandler(LOG_FILE_HANDLER)',
        '\n',
        'logger = AppLogger().logger'
    ]
    src_dir = get_src_dir(project_name, mode)
    logger_file = join(src_dir, 'app_logger.py')
    data = '\n'.join(content)
    new_file(logger_file, data)


def new_src_app(project_name, mode='project'):
    """ 
    root_dir/src/app.py
    """
    content = [
        'from .app_config import config',
        'from .app_logger import logger, BASIC_FORMAT',
        '\n',
        'import logging',
        'import json',
        '\n',
        'class App():',
        '    def __init__(self):',
        '        if config.DEBUG:',
        '            logging.basicConfig(level=logging.DEBUG, format=BASIC_FORMAT)',
        '        else:',
        '            logging.basicConfig(level=logging.ERROR, format=BASIC_FORMAT)',
        '        PRODUCT = json.dumps(config.__dict__, indent=4)',
        '        logger.info("----------------------------------------------------")',
        '        if config.DEBUG:',
        '            logger.debug(PRODUCT)',
        '        else:',
        '            logger.info(f"DEBUG: {config.IS_DEBUG}")',
        '        logger.info("----------------------------------------------------")',
        '        logger.debug("APP RUNNING")'
        '\n',
        '    def run(self):',
        '        pass'
    ]
    if mode == 'module':
        content = [
            '"""',
            '在 __init__.py 进行对外导出',
            '"""'
        ]
    src_dir = get_src_dir(project_name, mode)
    app_file = join(src_dir, 'app.py')
    data = '\n'.join(content)
    new_file(app_file, data)


def new_src_init(project_name, mode='project'):
    """
    root_dir/src/__init__.py 
    """
    content = 'from .app import App'
    if mode == 'module':
        content = '# EXPOSRTS MODULE CLASS OR FUNCTION'
    src_dir = get_src_dir(project_name, mode)
    init_file = join(src_dir, '__init__.py')
    new_file(init_file, content)


def new_project_src(project_name):
    """
    Export Project 
    """
    new_src_dir(project_name)
    new_src_config(project_name)
    new_src_static(project_name)
    new_src_logger(project_name)
    new_src_app(project_name)
    new_src_init(project_name)


def new_module_src(project_name):
    """
    Export Module  
    """
    mode = 'module'
    new_src_dir(project_name,mode)
    new_src_config(project_name, mode)
    new_src_static(project_name, mode)
    new_src_app(project_name, mode)
    new_src_init(project_name, mode)
