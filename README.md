# 基于网络词典的现代汉语词义消歧数据集构建(Construction of a Modern Chinese Word Sense Dataset Based on Online Dictionaries)


## 简介

词义消歧作为自然语言处理最经典的任务之一,旨在识别多义词在给定上下文中的正确词义。相比英文,中文的一词多义现象更普遍,然而当前公开发布的汉语词义消歧数据集很少。本文爬取并融合了两个公开的网络词典,并从中筛选1083个词语和相关义项作为待标注对象。进而,从网络数据及专业语料中为抽取相关句子。最后,以多人标注、专家审核的方式进行了人工标注。数据集1包含将近2万个句子,即每个词平均对应约20个句子。本文将数据集划分为训练集、验证集和测试集,对多种模型进行实验对比。


注：本研究更新了数据集的划分规则，以更好的适配当前词义消歧任务的需要。目前各数据集已公布，但由于本工作是“多选”形式的词义消歧数据，GlossBERT、BEM和ESCHER在使用该数据集时需做一定修改，目前已上传了GlossBERT和ESCHER的修改代码。**值得一提的是，ESCHER模型是当前在本数据集上效果最好的模型，如果后续有模型上的优化，建议基于该模型做尝试。**


CCL结果中GlossBERT模型F值过低，这是由于之前的PRF评判脚本没有顾及本数据的“多选问题”，导致许多结果欠召，新的评判脚本已解决这一问题。


如果近期有数据使用上的困扰，可直接联系电子邮箱：2115621341@qq.com。


**近期关注到一个不错的中文词义消歧数据集工作：  MiCLS**    https://github.com/COOLPKU/MSD_task

Modern Chinese Word Sense Annotated dataset构建的初衷是聚焦于“Gloss”（释义），希望更多的释义能对Transformer类模型有更多帮助。不过也被吐槽反馈“多选”形式存在模型难适配、与前人工作难比较的问题。MiCLS作为近期另一个已公开的中文词义消歧数据集同样有着不错的规模，在使用本数据集困难时也可选择MiCLS做更进一步研究。

最后，衷心希望 Chinese WSD 能有更多优秀的数据集和模型工作。

## 文件介绍


* Chinese_wsd_final    ：    基于论文中规则构建的现代汉语词义消歧数据集，一个例句可能对应多个词义
* wsd_multi_sense_only_final    ：    与Chinese_wsd_final对应的词语词义集合
* wsd_single_sense_sentence_final    ：    根据一些合并规则将Chinese_wsd_final中数据变为单选形式，即每个例句仅对应一个词义，且词义也进行了合并
* Dataset_ALL    :    划分好的训练集、验证集和测试集。
* GlossBERT-master    ：    修改后以适配该数据的GlossBERT模型。
* esc-master-chinese    :    修改后以适配该数据的ESCHER模型。    

## 实验结果

由于本次数据集划分规则与CCL论文中不同，因此实验结果会与CCL中的结果有出入，具体实验结果如下：

| Model     | Dev       | Tets      | MFS       | HFS       | Few-shot  | Zero-shot |
|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| GlossBERT | 69.93     | 70.51     | 91.73     | 79.82     | 43.10     | 41.28     |
| BEM       | 70.98     | 71.82     | **92.98** | 80.21     | 46.48     | 44.73     |
| ESCHER    | **75.85** | **76.63** | 91.41     | **83.64** | **55.72** | **50.47** |

注：每个模型分别取三个随机数进行实验，最后实验结果为三次实验结果的平均值。
由于实验室计算资源有限，本工作的模型仅在1-2个1080Ti上进行，batchsize及max_seq_length设置不是很高，如果计算资源足够，适当增大batch_size及max_seq_length，模型结果可能会有一定幅度的提升。

**所列结果仅用于验证所构建数据集的合理性和可用性，您可根据当前工作需求对数据集自行划分**


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
