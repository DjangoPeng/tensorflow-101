<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [TensorFlow 快速入门与实战](#tensorflow-%E5%BF%AB%E9%80%9F%E5%85%A5%E9%97%A8%E4%B8%8E%E5%AE%9E%E6%88%98)
  - [课件列表](#%E8%AF%BE%E4%BB%B6%E5%88%97%E8%A1%A8)
  - [问题答疑](#%E9%97%AE%E9%A2%98%E7%AD%94%E7%96%91)
      - [1. Windows 上安装 TensorFlow 流程](#1-windows-%E4%B8%8A%E5%AE%89%E8%A3%85-tensorflow-%E6%B5%81%E7%A8%8B)
      - [2. 学这个课程需要什么样的基础？](#2-%E5%AD%A6%E8%BF%99%E4%B8%AA%E8%AF%BE%E7%A8%8B%E9%9C%80%E8%A6%81%E4%BB%80%E4%B9%88%E6%A0%B7%E7%9A%84%E5%9F%BA%E7%A1%80)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# TensorFlow 快速入门与实战

![](images/course_poster.jpg)

## 课件列表

[第一部分：TensorFlow初印象](slides/1-TensorFlow初印象.pdf)

[第二部分：TensorFlow初接触](slides/2-TensorFlow初接触.pdf)

[第三部分：TensorFlow基础概念解析](slides/3-TensorFlow基础概念解析.pdf)

## 问题答疑

**我将极客时间上多次提到的问题整理在此，希望可以解答有同样问题的朋友。**

#### 1. Windows 上安装 TensorFlow 流程

对于有英文基础的朋友，建议直接阅读官网[安装教程](https://www.tensorflow.org/install/pip?lang=python3)。本答案翻译自 TensorFlow 官网。

系统环境要求：
 - Windows 7（64位) 以上版本
 - Python 3.4, 3.5 或 3.6

Windows 上安装 TensorFlow 步骤：
1. 安装 Python 开发环境

检查系统是否已安装 Python 开发环境。如果已安装，则跳过该步骤。
```shell
python3 --version
pip3 --version
virtualenv --version
```

1) 独立安装 Microsoft Visual C++ 2015 Redistributable Update 3 或安装完整的 Visual Studio 2015：
- 进入 Visual Studio [下载页](https://visualstudio.microsoft.com/vs/older-downloads/)
- 选择 **Redistributables and Build Tools**
- 下载和安装 Microsoft Visual C++ 2015 Redistributable Update 3

2) 安装 Windows 上 [64位的 Python 3 发布版](https://www.python.org/downloads/windows/)
3) 安装 **pip** 和 **virtualenv**

```shell
pip3 install -U pip virtualenv
```

2. 创建 Python 虚拟环境

```shell
virtualenv --system-site-packages -p python3 ./venv
.\venv\Scripts\activate
pip install --upgrade pip
pip list  # 展示 venv 中已安装的软件包
deactivate  # 使用完 TensorFlow 后，方可推出 venv 虚拟环境
```

3. 安装 TensorFlow pip 包

```shell
pip install --upgrade tensorflow
python -c "import tensorflow as tf; tf.enable_eager_execution(); print(tf.reduce_sum(tf.random_normal([1000, 1000])))"
```

#### 2. 学这个课程需要什么样的基础？

1. 编程语言：Python 基础语法，不需要太高深技巧，因为是 DSL
2. 数学：线性代数、数学分析（或微积分）、简单的统计学基础
3. AI：基础的神经网络理论