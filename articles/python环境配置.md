![](https://img2020.cnblogs.com/blog/2170201/202010/2170201-20201015110629690-682595215.jpg)

---

# 零、参考

&nbsp;

> [python-tutorial](https://code.visualstudio.com/docs/python/python-tutorial)

> [powershell下的编码问题](https://stackoverflow.com/questions/35176270/python-2-7-lookuperror-unknown-encoding-cp65001)

&nbsp;

# 一、下载安装python

&nbsp;

[python2.7.18 Windows x86-64 MSI installer](https://www.python.org/ftp/python/2.7.18/python-2.7.18.amd64.msi)

[python3.8.6 Windows x86-64 executable installer](https://www.python.org/ftp/python/3.8.6/python-3.8.6-amd64.exe)

安装完成后

python2.exe 路径为 `/g/python/python2/python2.7.18/python.exe`

python3.exe 路径为 `/g/python/python3/python3.8.6/python.exe`

&nbsp;

# 二、下载安装vscode

&nbsp;

[vscode download](https://code.visualstudio.com/Download)

&nbsp;

# 三、python配置项

&nbsp;

### 3.1 默认配置

![](https://img2020.cnblogs.com/blog/2170201/202010/2170201-20201015114102841-1931900618.png)

```
{
    "powermode.enabled": true,
    "[python]": {},
    "python.pythonPath": "G:/python/python2/python2.7.18/python.exe", # python解释器默认配置
    "python.autoComplete.extraPaths": [],
}
```

### 3.2 特定配置

可以在项目目录下，创建文件 `.vscode/settings.json`, 内容如下:

```
{
    "python.pythonPath": "G:/python/python2/python2.7.18/python.exe"
}
```

&nbsp;

# 四、python虚拟环境配置

&nbsp;

###  

### 3.1 利用pip 安装pyenv

```
# powershell命令
PS G:\> .\python\python3\python3.8.6\Scripts\pip.exe install pyenv-win --target G:\pyenv
# 将可执行文件目录添加到windows的Administrator环境配置中
# (1) G:\pyenv\pyenv-win\bin ; (2) G:\pyenv\pyenv-win\shims
```

### 3.2 利用pyenv 安装不同版本的python

(1) 修改pyenv使用的镜像为淘宝源（加速）

a. 修改文件`G:\pyenv\pyenv-win\libexec\libs\pyenv-install-lib.vbs`中的`mirror`

```
Dim mirror
' mirror = objws.Environment("Process")("PYTHON_BUILD_MIRROR_URL")
' If mirror = "" Then mirror = "https://www.python.org/ftp/python"

mirror = "https://npm.taobao.org/mirrors/python"
```

注意：这个修改没有实际作用

b. 修改文件`G:\pyenv\pyenv-win\.versions_cache.xml`中的`URL`对象中的镜像链接

&nbsp;

(2) 安装python的各个版本

```
pyenv install 2.7.16

pyenv install 2.7.17

pyenv install 3.8.2
```

### 3.3 利用virtualenv安装虚拟环境

&nbsp;

(1) 利用pip安装virtualenv

```
/g/pyenv/pyenv-win/versions/2.7.17/Scripts/pip.exe install virtualenv -t /g/pyenv/virtualenv

```

&nbsp;

(2) 将virtualenv添加到windows的系统环境变量

`/g/pyenv/virtualenv/bin`

&nbsp;

(3) 创建虚拟环境

```
virtualenv.exe /g/pyenv/envs/yzp2env -p /g/pyenv/pyenv-win/versions/2.7.17/python.exe
```

&nbsp;

(4) 在`vscode`的`settings.json`中配置虚拟环境

```
{
    "python.pythonPath": "G:/pyenv/envs/yzp2env/Scripts/python.exe",
}
```

# 五、插件推荐


### 5.1 `Power Mode`

输入时候有炫酷的特效

### 5.2 `vscode-icons`

项目中的文件都有对应的icon

### 5.3 `Path Intellisense`

路径自动补全(模块、文件)

### 5.4 `Bracket Pair Colorizer`

多层括号显示不同的颜色






