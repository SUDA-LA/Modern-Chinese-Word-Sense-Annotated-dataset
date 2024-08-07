# GlossBERT 适配

## 前言

GlossBERT模型原代码地址：https://github.com/HSLCY/GlossBERT 。该文档旨在将改模型适配在本项目的数据上。

## 模型训练

*  请根据原模型需求配置环境。
*  训练请使先修改/run.sh中配置。
*  /Data中包含了适配GlossBERT的本项目数据。


## 模型测试

*  在eval时该模型会输出一个预测文档，需要对该文档在外部调用脚本才能做PRF评估。脚本今晚添加（2024.8.7）
