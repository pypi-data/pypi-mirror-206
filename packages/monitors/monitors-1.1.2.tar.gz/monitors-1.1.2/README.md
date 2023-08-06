# monitors


[![Build Status](https://travis-ci.com/Pactortester/monitors.svg?branch=master)](https://travis-ci.com/Pactortester/monitors) ![PyPI](https://img.shields.io/pypi/v/monitors) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/monitors) ![GitHub top language](https://img.shields.io/github/languages/top/Pactortester/monitors) [![Downloads](https://pepy.tech/badge/monitors)](https://pepy.tech/project/monitors) ![GitHub stars](https://img.shields.io/github/stars/Pactortester/monitors?style=social) ![https://blog.csdn.net/flower_drop](https://img.shields.io/badge/csdn-%40flower__drop-orange)


## Logo


![](https://files.mdnice.com/user/17535/0ce07240-b2ea-4739-aede-b67a2bc8b757.png)


##  仓库地址：


- github：https://github.com/Pactortester/monitors.git
- pypi：https://pypi.org/project/monitors/#history

## 背景介绍
专项测试，桌面端应用程序使用过程中，对CPU，内存，磁盘使用率，网络流量进行监控并展现.

## 解决方案

### 需求梳理
1. 简单方便 傻瓜式操作
2. 数据持久化，数据可保存
3. 数据可视化，清晰明了

解决方案来了，如下
>minitor作为监控服务，influxdb做为数据收集，Grafana图表可视化展示，干就完了！

## 前提准备
1. 你需要安装好 influxdb
2. 你还需要安装好 grafana

>看到这，你是不是又慌乱了，怎么还需要这么多准备工作。莫慌，教程都给你准备好了，乖，张开嘴，吃～

- [Linux下安装配置Grafana压测监控服务-安装InfluxDB
](https://mp.weixin.qq.com/s?__biz=MzIxMjE1ODAzOA==&mid=2650631463&idx=1&sn=cc3125d39b5559eca88a23ed1e7164d9&chksm=8f439e1eb83417083a98da8bd717fcfe2f5399e4f6c7ec031be61812562544956256965182d7&token=430212778&lang=zh_CN#rd)
- [Linux下安装配置Grafana压测监控服务-安装Grafana](https://mp.weixin.qq.com/s?__biz=MzIxMjE1ODAzOA==&mid=2650631478&idx=1&sn=df8f41d086d7421400e9ea4673d9f3cc&chksm=8f439e0fb834171908af65152a9b4de25f648809f5dea1877a650835f968732540c9bd34d744&token=430212778&lang=zh_CN#rd)

## 安装服务
```
pip install -U monitors
```


## 启动服务

```python
# -*- coding: utf-8 -*-
"""
@Project ：monitors 
@File    ：monitor.py
@Author  ：lijiawei
@Date    ：2021/9/6 4:13 下午 
"""

from monitors.monitor_set import Settings as ST
import argparse


parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument("-name", type=str)

args = parser.parse_args()
name = args.name

# 服务端ip
ST.host = '127.0.0.1'
# influxdb 端口
ST.port = 8086
# influxdb 账号
ST.password = '*********'
# influxdb 数据库
ST.database = 'test_database'
# Grafana apikey
ST.apikey = '********'
# influxdb 表
ST.table = name

from monitors.monitor_util import monitor_on

monitor_on()
```


>注意：脚本内容禁止任何修改！

## 运行命令

```
python monitor.py -name=test_monitor

```

![](https://files.mdnice.com/user/17535/315d2617-bcbc-4497-a258-effa717d6521.png)

>参数说明：name 必须为唯一值

## 查看结果

打开 Grafana url 登录后 查看监控图表

![](https://files.mdnice.com/user/17535/aaa6a355-d8e6-4847-9049-474a45040989.png)

>Grafana账号密码：test/test

## 停止监控
按下 CTRL + C，监控服务已停止！


![](https://files.mdnice.com/user/17535/dce8bbb5-2a5c-4ac6-abac-4f9f8c43a620.png)

## 后续方案

在推广使用过程中，发现尽管已经做的如此简单，还是有同学不会使用，一步三个坑，后续我计划把【minitors】监控服务，打包成可执行文件，有完整的页面交互，防止大家掉坑！

## 视频分析

```
          点击应用图标              弹窗1   关闭弹窗1     欢迎页     滑动欢迎页    弹窗2    关闭弹窗2   首页
              ^                     ^                   ^                     ^                  ^ 
              |                     |                   |                     |                  |
              |---------logo1-------|-------logo2-------|--------.......------|------......------|

稳定阶段（个）： 2         1          1         1          1                     1                  2

              |                     |                   |                     |                  |
              v                     v                   v                     v                  v
              A                     B                   C                     D                  E
```

## 

以上便是 monitors 的基本用法介绍。

如果您有发现错误，或者您对 monitors 有任何建议，欢迎到 [monitors Issues](https://github.com/Pactortester/monitors/issues) 发表，非常感谢您的支持。您的反馈和建议非常宝贵，希望您的参与能帮助 monitors 做得更好。
