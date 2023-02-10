#!/usr/bin/env bash

# ACTIVATE VIRTUAL ENVIRONMENT
module load conda/5.0.1-python3.6 
module load cuda/10.2
source activate argmin


# SELECT TASK

# 1) SEQUENCE TAGGING
#export TASK_NAME=seqtag
#export MODELTYPE=bert-seqtag

# 2) RELATION CLASSIFICATION
export TASK_NAME=relclass
#export TASK_NAME=outcomeclf
#export MODELTYPE=bertweighted
export MODELTYPE=robertaweighted

# 3) MULTIPLE CHOICE
#export TASK_NAME=multichoice
#export MODELTYPE=bert-multichoice


#export DATA_DIR=data/neoplasm/
#export DATA_DIR=data/outcome/
export DATA_DIR=data/train/

export MAXSEQLENGTH=64
export OUTPUTDIR=output/Robertaweighted$TASK_NAME$MAXSEQLENGTH/

# TRAIN MODEL
# CHOOSE BERT MODEL
#export MODEL=monologg/biobert_v1.1_pubmed
#export MODEL=allenai/scibert_scivocab_cased
#export MODEL=allenai/scibert_scivocab_uncased
#export MODEL=bert-base-cased
#export MODEL=bert-base-uncased
export MODEL=roberta-base



# EVALUATE MODEL:
# SET OUTPUTDIR TO MODELDIR AND REMOVE --do_train
#export MODEL=output/seqtag256bioBERT/
#export OUTPUTDIR=$MODEL

echo $CWD

#python train_multiplechoice.py \
#--do_lower_case \

python train_weighted.py \
--model_type $MODELTYPE \
--model_name_or_path $MODEL \
--output_dir $OUTPUTDIR \
--task_name $TASK_NAME \
--do_lower_case \
--do_train \
--do_eval \
--data_dir $DATA_DIR \
--max_seq_length $MAXSEQLENGTH \
--overwrite_output_dir \
--per_gpu_train_batch_size 16 \
--learning_rate 2e-5 \
--num_train_epochs 5.0 \
--save_steps 1000 \
--overwrite_cache
