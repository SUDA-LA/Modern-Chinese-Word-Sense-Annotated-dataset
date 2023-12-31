# 基于网络词典的现代汉语词义消歧数据集构建(Construction of a Modern Chinese Word Sense Dataset Based on Online Dictionaries)


## 简介

词义消歧作为自然语言处理最经典的任务之一,旨在识别多义词在给定上下文中的正确词义。相比英文,中文的一词多义现象更普遍,然而当前公开发布的汉语词义消歧数据集很少。本文爬取并融合了两个公开的网络词典,并从中筛选1083个词语和相关义项作为待标注对象。进而,从网络数据及专业语料中为抽取相关句子。最后,以多人标注、专家审核的方式进行了人工标注。数据集1包含将近2万个句子,即每个词平均对应约20个句子。本文将数据集划分为训练集、验证集和测试集,对多种模型进行实验对比。


## 文件介绍

本项目总共包含三个文件（均以json文件存储）：

* Chinese_wsd_final  ：  基于论文中规则构建的现代汉语词义消歧数据集，一个例句可能对应多个词义
* wsd_multi_sense_only_final   ： 与Chinese_wsd_final对应的词语词义集合
* wsd_single_sense_sentence_final     ： 根据一些合并规则将Chinese_wsd_final中数据变为单选形式，即每个例句仅对应一个词义，且词义也进行了合并



## Citation:

```
@inproceedings{yan-etal-2023-ji,
    title = "基于网络词典的现代汉语词义消歧数据集构建(Construction of a {M}odern {C}hinese Word Sense Dataset Based on Online Dictionaries)",
    author = "Yan, Fukang  and
      Zhang, Yue  and
      Li, Zhenghua",
    booktitle = "Proceedings of the 22nd Chinese National Conference on Computational Linguistics",
    month = aug,
    year = "2023",
    address = "Harbin, China",
    publisher = "Chinese Information Processing Society of China",
    url = "https://aclanthology.org/2023.ccl-1.4",
    pages = "43--53",
    abstract = "{``}词义消歧作为自然语言处理最经典的任务之一,旨在识别多义词在给定上下文中的正确词义。相比英文,中文的一词多义现象更普遍,然而当前公开发布的汉语词义消歧数据集很少。本文爬取并融合了两个公开的网络词典,并从中筛选1083个词语和相关义项作为待标注对象。进而,从网络数据及专业语料中为抽取相关句子。最后,以多人标注、专家审核的方式进行了人工标注。数据集1包含将近2万个句子,即每个词平均对应约20个句子。本文将数据集划分为训练集、验证集和测试集,对多种模型进行实验对比。{''}",
    language = "Chinese",
}

```
