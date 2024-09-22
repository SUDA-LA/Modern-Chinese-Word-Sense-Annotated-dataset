# 基于网络词典的现代汉语词义消歧数据集构建(Construction of a Modern Chinese Word Sense Dataset Based on Online Dictionaries)


## 简介

词义消歧作为自然语言处理最经典的任务之一,旨在识别多义词在给定上下文中的正确词义。相比英文,中文的一词多义现象更普遍,然而当前公开发布的汉语词义消歧数据集很少。本文爬取并融合了两个公开的网络词典,并从中筛选1083个词语和相关义项作为待标注对象。进而,从网络数据及专业语料中为抽取相关句子。最后,以多人标注、专家审核的方式进行了人工标注。数据集1包含将近2万个句子,即每个词平均对应约20个句子。本文将数据集划分为训练集、验证集和测试集,对多种模型进行实验对比。


注：本研究更新了数据集的划分规则，以更好的适配当前词义消歧任务的需要。目前各数据集已公布，但由于本工作是“多选”形式的词义消歧数据，GlossBERT、BEM和ESCHER在使用该数据集时需做一定修改，目前已上传了GlossBERT和ESCHER的修改代码（2024.8.4记录）。值得一提的是，ESCHER模型是当前在本数据集上效果最好的模型，如果后续有模型上的优化，建议基于该模型做尝试。

由于本次数据集划分规则与CCL论文中不同，因此实验结果会与CCL中的结果有出入，具体实验结果会在本周放入该页面，如果近期需求较急，可直接邮件联系我，（2024.8.7记录）

CCL结果中GlossBERT模型F值过低，这是由于之前的PRF评判脚本没有顾及本数据的“多选问题”，导致许多结果欠召，新的评判脚本已解决这一问题。

* TOADD：新数据集下的实验结果
* TOADD：新旧数据集划分规则对比

如果近期有数据使用上的困扰，可直接联系电子邮箱：2115621341@qq.com。


## 文件介绍


* Chinese_wsd_final    ：    基于论文中规则构建的现代汉语词义消歧数据集，一个例句可能对应多个词义
* wsd_multi_sense_only_final    ：    与Chinese_wsd_final对应的词语词义集合
* wsd_single_sense_sentence_final    ：    根据一些合并规则将Chinese_wsd_final中数据变为单选形式，即每个例句仅对应一个词义，且词义也进行了合并
* Dataset_ALL    :    划分好的训练集、验证集和测试集。
* GlossBERT-master    ：    修改后以适配该数据的GlossBERT模型。
* esc-master-chinese    :    修改后以适配该数据的ESCHER模型。    

## 实验结果

| k | ALL   | MFS   | LFS   | Few-shot | Zero-shot |
|---|-------|-------|-------|----------|-----------|
| 3 | 76.94 | 91.41 | 83.58 | 56.63    | 50.45     |




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
