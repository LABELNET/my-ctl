#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
   @File    :   app_dir_ai.py
   @Create  :   2023/03/14 14:35:47
   @Author  :   Yuan Mingzhuo
   @Update  :   2023/03/14
   @License :   (C)Copyright 2014-2023 YuanMingZhuo All Rights Reserved 
   @Desc    :   AI Project Template
"""

from os import mkdir, getcwd
from os.path import join, exists

"""
Basic Module
---
- datasets  , 数据集
- model , 模型
- train , 训练
- inference , 推理
- tools , 工具库
"""


def new_file(file_name, data):
    """
    create new file
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(data)


def new_datasets(project_name):
    """
    root_dir/datasets 
    """
    dataset_dir = join(getcwd(), project_name, 'datasets')
    if not exists(dataset_dir):
        mkdir(dataset_dir)
    content = '# DATASETS DOWNLOAD AND PREPROCESS'
    content_file = join(dataset_dir, '__init__.py')
    new_file(content_file, content)


def new_model(project_name):
    """
    root_dir/model
    """
    model_dir = join(getcwd(), project_name, 'model')
    if not exists(model_dir):
        mkdir(model_dir)
    content = '# MODEL DEV'
    content_file = join(model_dir, '__init__.py')
    new_file(content_file, content)


def new_train(project_name):
    """
    root_dir/train 
    """
    train_dir = join(getcwd(), project_name, 'train')
    if not exists(train_dir):
        mkdir(train_dir)
    content = '# train model and train tools'
    content_file = join(train_dir, '__init__.py')
    new_file(content_file, content)


def new_inference(project_name):
    """
    root_dir/inference 
    """
    inference_dir = join(getcwd(), project_name, 'inference')
    if not exists(inference_dir):
        mkdir(inference_dir)
    content = '# model inference and inference tools'
    content_file = join(inference_dir, '__init__.py')
    new_file(content_file, content)

def new_tools(project_name):
    """
    root_dir/tools 
    """
    tools_dir = join(getcwd(), project_name, 'tools')
    if not exists(tools_dir):
        mkdir(tools_dir)
    content = '# visual and tracker tools'
    content_file = join(tools_dir, '__init__.py')
    new_file(content_file, content)

def new_main(project_name):
    """
    root_dir/main.py  
    """
    content = [
        '\n',
        '"""',
        "Main function , import other package methods",
        '"""',
        '\n',
        '\n',
        'if __name__=="__main__":',
        '    pass'
    ]
    data = '\n'.join(content)
    content_file = join(getcwd(),project_name, 'main.py')
    new_file(content_file, data)
    
def new_ai(project_name):
    """
    Export Methods 
    """
    new_datasets(project_name)
    new_model(project_name)
    new_train(project_name)
    new_inference(project_name)
    new_tools(project_name)
    new_main(project_name)