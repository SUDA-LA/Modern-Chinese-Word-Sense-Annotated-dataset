export PYTHONPATH=$(pwd)
CUDA_VISIBLE_DEVICES=0 nohup  python esc/train.py \
    --run_name YOUR_RUNNAME  \
    --add_glosses_noise \
    --tokens_per_batch 512 \
    --validation_path YOUR_VAL_DATA \
    --transformer_model YOUR_MODEL \
    --chinese_dic YOUR_DICT \
    --train_path YOUR_TRAIN_DATA  > RESULT.log 2>&1 &