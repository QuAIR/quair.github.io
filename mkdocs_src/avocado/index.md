# Avocado

QuAIR 团队的量子计算研究平台（建设中）

## 结构介绍

- `avocado`: 主模块，含以下子模块/接口

  - `ansatz`: 电路模板设计
  - `core`: 核心逻辑计算
  - `database`: 量子数据库
  - `operator`: 量子操作集
    - `channel`: 量子信道集
    - `gate`: 量子门集
  - `circuit`: 量子电路接口
  - `qinfo`: 量子算法/信息工具集
  
- `docs`: API 生产目录
- `tests`: 单元测试集

## 功能

- QNN 算法模拟
- 量子电路模拟 & 展示
- 量子信道模拟
- 量子算法/信息工具集

## 安装方法

### 安装 Avocado

首先安装/激活 anaconda 环境的指令

```bash
conda create -n avocado python=3.10
conda activate avocado
conda install jupyter notebook # 配置 jupyter 环境
```

使用 `pip install -e .` 安装 avocado。具体代码如下

```bash
cd "C:\Users\#YOUR NAME HERE#\Avocado-Dev" # 切换到代码库文件夹所在位置
pip install -e . # 安装 avocado
```

### 链接 MATLAB

> 请注意 MATLAB 版本兼容不同的 Python 版本。详见[官方文档](https://ww2.mathworks.cn/support/requirements/python-compatibility.html)。

可以使用下列指令链接最新版 MATLAB

```bash
pip install matlabengine # 如使用最新版 MATLAB，则使用该指令安装
```

若你正在使用旧版 MATLAB, 则上述指令会弹出 error 信息。该信息会包括

```text
RuntimeError: No compatible MATLAB installation found in Windows Registry. This release of MATLAB Engine API for Python is compatible with version yy.y. The found version were xx.x.
```

此时，改运行下列指令即可。

```bash
pip install matlabengine==xx.x.1
```

## 本地打开Avocado的API文档

在 bash 环境中运行以下指令，运行完成后API文档就会自动打开：
```bash
cd "C:\Users\#YOUR NAME HERE#\QuAIR-platform" # 切换到代码库文件夹所在位置
./api.sh # 输入此指令回车后稍等会更新
```

API文档首页位置在
`\docs\api\index.html`
