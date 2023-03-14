#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
   @File    :   app_template_py.py
   @Create  :   2023/03/14 08:39:59
   @Author  :   Yuan Mingzhuo
   @Update  :   2023/03/14
   @License :   (C)Copyright 2014-2023 YuanMingZhuo All Rights Reserved 
   @Desc    :   Coding Below
"""
from os import mkdir, getcwd
from os.path import join, exists
import yaml


def new_file(file_name, data):
    """
    create new file
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(data)


def new_project_dir(project_name, mode='project'):
    """
    root_dir
    """
    # root
    project_path = join(getcwd(), project_name)
    if exists(project_path):
        return
    mkdir(project_path)

def new_gitignore(project_name):
    """ 
    root_dir/.gitignore
    """
    content = [
        '__pycache__',
        'dist',
        'build',
        'outputs',
        '*.onnx',
        '*.engine',
        '*.weights',
        '*.pth',
        '*.pdparams',
        '*.mp4',
        '*.mov',
        '*.flv',
        '*.egg-info',
        '*.log',
        '.pytest_cache',
        '.vscode',
        'setup.py'
    ]
    file = join(getcwd(), project_name, '.gitignore')
    data = '\n'.join(content)
    new_file(file, data)


def new_config(project_name, mode='project'):
    """
    root_dir/config.yaml
    """
    package_name = str(project_name).replace('-', '_')
    build_src = 'app'
    if mode == 'module':
        build_src = package_name
    project_data = {
        'name': f'{project_name}',
        'mode': mode,
        'version': '1.0.0',
        'description': 'this is version desc',
        'author': 'labelnet',
        'author_email': 'labelnet@foxmail.com',
        'license': 'labelnet',
        'python': '>=3.6',
        'keywords': [
            f'{package_name}'
        ],
        'requirements': [
            'requests==2.25.1',
            'pytest==6.2.5',
            'pyyaml==6.0'
        ],
        'build': {
            'src': f'{build_src}',
            'static': 'static',
            'environ_static': f'{package_name}_static'
        }
    }
    env_data = {
        'debug': {
            "DEBUG": True,
            "PROJECT_NAME": f'{project_name}'
        },
        'product': {
            "DEBUG": False,
            "PROJECT_NAME": f'{project_name}'
        }
    }
    
    config_data = {
        'project': project_data
    }
    if mode == 'project':
        config_data['environments'] = env_data
    # save
    config_file = join(getcwd(), project_name, 'config.yaml')
    data = yaml.dump(config_data, indent=2, sort_keys=False)
    new_file(config_file, data)


def new_license(project_name):
    """
    root_dir/LICENSE 
    """
    content = [
        f'(C)Copyright {project_name} All Rights Reserved',
        f'Project intellectual property belongs to {project_name} , Can not be passed without permission.'
    ]
    license_file = join(getcwd(), project_name, 'LICENSE')
    data = '\n'.join(content)
    new_file(license_file, data)


def new_readme(project_name):
    """
    root_dir/README.md 
    """
    content = [
        f'# {project_name}',
        '\n Please edit project infos \n',
        '## Build',
        '\n build desc \n',
        '## Use',
        '\n use desc , try run `python main.py` or try test `python test.py` \n',
        '## FQA',
        '\n QA desc \n'
    ]
    readme_file = join(getcwd(), project_name, 'README.md')
    data = '\n'.join(content)
    new_file(readme_file, data)


def new_requiremennts(project_name):
    """ 
    root_dir/requirements.txt
    """
    content = [
        'requests==2.25.1',
        'nuitka==0.6.17.4',
        'pytest==6.2.5',
        'myctl'
    ]
    requirements_file = join(getcwd(), project_name, 'requirements.txt')
    data = '\n'.join(content)
    new_file(requirements_file, data)

def new_main(project_name):
    """
    root_dir/main.py 
    """
    content = [
        'from app import App',
        '\n',
        'if __name__=="__main__":',
        '    App().run()'
    ]
    main_file = join(getcwd(), project_name,'main.py')
    data = '\n'.join(content)
    new_file(main_file,data)

def new_test(project_name):
    """
    root_dir/test.py 
    """
    content = [
        'import pytest',
        '\n',
        'if __name__=="__main__":',
        '    pytest.main(["tests","-s"])',
        '    # pytest.main(["tests/test_app.py","-s"])'
    ]
    test_file = join(getcwd(), project_name,'test.py')
    data = '\n'.join(content)
    new_file(test_file,data)

def new_dockerfile(project_name):
    """
    root_dir/Dockerfile 
    """
    content = [
        'FROM python:3.8-slim',
        '\n',
        'ENV TZ=Asia/Shanghai',
        'RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone',
        '# 系统环境',
        'RUN sed -i s@/deb.debian.org/@/mirrors.aliyun.com/@g /etc/apt/sources.list \ ',
        '    && apt-get clean \ ',
        '    && apt-get update \ ',
        '    && apt-get install -y sudo curl wget inetutils-ping net-tools build-essential libgl1-mesa-glx libglib2.0-dev',
        '\n',
        'WORKDIR /app',
        '# 安装依赖',
        'COPY ./requirements.txt /app/',
        'RUN pip install -r /app/requirements.txt -i https://pypi.douban.com/simple',
        'RUN pip install myctl ',
        '\n',
        '# 源码编译',
        'COPY . /app/code/',
        'RUN cd /app/code/ && myctl build --env product',
        'RUN cp -rf /app/code/build /app/ && rm -rf /app/code &&  mv /app/build /app/code',
        '\n',
        '# 运行',
        'CMD ["/app/code/app.bin"]'
    ]
    dockerfile_file = join(getcwd(),project_name,'Dockerfile')
    data = '\n'.join(content)
    new_file(dockerfile_file,data)

def new_dockerignore(project_name):
    """
    root_dir/.dockerignore
    """
    content = [
        '.vscode',
        '__pycache__',
        'Dockerfile',
        'README.md',
        '*.mp4',
        '*.mov',
    ]
    dockerignore = join(getcwd(),project_name,'.dockerignore')
    data = '\n'.join(content)
    new_file(dockerignore,data)


def new_project(project_name):
    """
    Export Project
    """
    # root_dir
    new_project_dir(project_name)
    # root_dir/.gitignore
    new_gitignore(project_name)
    # root_dir/config.yaml
    new_config(project_name)
    # root_dir/LICENSE
    new_license(project_name)
    # root_dir/README.md
    new_readme(project_name)
    # root_dir/requirements.txt
    new_requiremennts(project_name)
    # root_dir/main.py
    new_main(project_name)
    # root_dir/test.py
    new_test(project_name)
    # root_dir/Dockerfile
    new_dockerfile(project_name)
    # root_dir/.dockerignore
    new_dockerignore(project_name)


def new_module(project_name):
    """ 
    Export Module
    """
    mode = 'module'
    # root_dir
    new_project_dir(project_name, mode)
    # root_dir/.gitignore
    new_gitignore(project_name)
    # root_dir/config.yaml
    new_config(project_name, mode)
    # root_dir/LICENSE
    new_license(project_name)
    # root_dir/README.md
    new_readme(project_name)
    # root_dir/requirements.txt
    new_requiremennts(project_name)
    # root_dir/test.py
    new_test(project_name)
    
