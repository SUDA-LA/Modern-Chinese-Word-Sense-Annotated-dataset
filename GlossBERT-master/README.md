# GlossBERT 适配

## 前言

GlossBERT模型原代码地址：https://github.com/HSLCY/GlossBERT 。该文档旨在将改模型适配在本项目的数据上。

## 模型训练

*  请根据原模型需求配置环境。
*  训练请使先修改/run.sh中配置。
*  /Data中包含了适配GlossBERT的本项目数据。
*  词典资源请使用根目录下的wsd_multi_sense_only_final.json


## 模型测试

*  在eval时该模型会输出一个预测文档，需要对该文档在外部调用脚本才能做PRF评估。
*  具体评估脚本见/GlossBERT_results/count_glossbert_F.py，使用时请替换对应文件路径。
*  /GlossBERT_results/result.txt 是一个结果例子，可用作count_glossbert_F的测试文档。
