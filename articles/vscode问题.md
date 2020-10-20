![](https://img2020.cnblogs.com/blog/2170201/202010/2170201-20201019152836305-1412097340.jpg)

&nbsp;

# 零、参考

&nbsp;

> ["Python was not found but can be installed from the Microsoft Store"](https://github.com/microsoft/vscode-python/issues/11981)

&nbsp;

# 一、问题

&nbsp;

### 1.1 python环境配置

&nbsp;

问题描述:

执行python代码时候报错，

```
[Running] python -u "g:\python_projects\yzpython\py_code\hello.py"
Python was not found but can be installed from the Microsoft Store: https://go.microsoft.com/fwlink?linkID=2082640
[Done] exited with code=9009 in 0.441 seconds
```

解决方式:

(1) 该问题是没有找到合适的python解释器造成的;

(2) 由于使用的python运行插件是 `Code Runner`，无法自动匹配解释器位置;

(3) 将运行插件替换为`python`，该问题解决

