export PYTHONPATH=$(pwd)
CUDA_VISIBLE_DEVICES=2 nohup python esc/predict.py \
    --ckpt /data1/fkyan/esc-master-chinese/experiments/roberta-large-627/lightning_logs/version_0/checkpoints/epoch=19_v0.ckpt \
    --prediction-types probabilistic \
    --dataset-paths /data1/fkyan/esc-master-chinese/data/Modern-Chinese-Word-Sense-Annotated-Corpus/test/test.data.txt\
    --chinese_dic /data1/fkyan/esc-master-chinese/data/Chinese_Ours_New_2/wsd_multi_sense_only.json \
    --evaluate > roberta-large-627-Test.log 2>&1 &