---
hide:
#   - navigation
#   - toc
---
> 可参考[量桨教程](https://qml.baidu.com/install/installation_guide.html)的本地安装方法。

首先安装/激活 anaconda 环境的指令

```bash
conda create -n avocado python=3.9
conda activate avocado
conda install jupyter notebook # 配置 jupyter 环境
```

参考量桨的本地安装方法，使用 `pip install -e .` 安装 avocado。具体代码如下

```bash
cd "C:\Users\#YOUR NAME HERE#\QuAIR-platform" # 切换到代码库文件夹所在位置
pip install -e . # 安装 avocado
```

可以使用下列指令链接 MATLAB

```bash
pip install matlabengine # 如使用最新版 MATLAB，则使用该指令安装
pip install matlabengine==9.14.2 # 如使用旧版，请查询对应版本可以使用的 matlabengine
```

最后运行 `test_grad.ipynb` 测试 avocado 是否安装成功。

## 更新Avocado的API文档

### 功能

更新Avocado函数API文档（HTML格式）

### 安装方法

用下列的指令安装更新API文档必要的库

```bash

pip install docutils==0.18.1
pip install sphinx-rtd-theme==1.3.0
pip install Sphinx==6.1.3
```