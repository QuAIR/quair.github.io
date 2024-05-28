---
hide:
  - navigation
#   - toc

---
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