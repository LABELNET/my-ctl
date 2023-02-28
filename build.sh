#!/bin/bash

# 删除临时文件
find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
# 权限
cp .pypirc ~/
chmod 600 ~/.pypirc
# 读取版本号
for version in $(cat VERSION)
do
  echo $version
done
# 打包上传
python setup.py check
python setup.py sdist bdist_wheel
python -m twine upload --repository my-ctl dist/*
# 复制版本打包列表
mv ./my_ctl.egg-info/SOURCES.txt ./version.info
# 删除缓存
rm -rf build
rm -rf dist
rm -rf *.egg-info
rm -rf ~/.pypirc