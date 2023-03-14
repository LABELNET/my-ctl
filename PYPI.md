## 上传包到 PYPI


```
# 编译
python main.py build --env product

# 上传
cd dist
twine upload dist/*

# 输入账户密码
```