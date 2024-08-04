# ESC  适配

## 前言



我们对ESCHER模型（原模型链接：https://github.com/SapienzaNLP/esc/tree/master ）做了中文数据的适配，使Modern-Chinese-Word-Sense-Annotated-dataset能够在该模型上使用。

值得一提的是ESCHER是目前在我们数据集上效果最好的WSD模型，由于本项目的数据集每个句子只包含一个待消歧词且未做词性、语义等标注，因此如ConSec之类的模型并不能在该数据集上使用，请在使用本项目的数据时注意使用限制。


## 模型训练

*  在模型训练前，请依据原模型的要求配置环境（可参考/requirements.txt）
*  模型训练时请将/run.sh中的参数替换为您所需的参数
*   /data中已根据模型要求对本项目的数据做了格式修改，可直接使用

