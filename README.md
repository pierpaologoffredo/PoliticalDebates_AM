# Argument extraction and classification on 50 years of U.S. political debates

In this repository, it is possible to find the source code to reproduce the experiments for the Argument Mining to detect components (*Claims*, *Premises*) and predict relations (*NoRelation*, *Attack*, *Support*) among them.

This work was made inspired by a similar [approach](https://gitlab.com/tomaye/ecai2020-transformer_based_am/).

In our work, we evaluate various transformer models for
1.  Argument Component Detection (Sequence Tagging Task), and
2.  Argument Relation Classification (Sequence Classification Task)

on **Political Debates**.

## Requirements/Setup
The code runs under Python 3.6 or higher. The required packages are listed in the requirements.txt, which can be directly installed from the file:
```
pip install -r /path/to/requirements.txt
```
Our code is based on the transformer library version 2.3.0. See https://github.com/huggingface/transformers for more details.

## Usage
To fine-tune a transformer model for detecting component, execute the following script. Models, tasks and hyper-parameters can be specified within the script.
```
sh run_train_component.sh
```

To fine-tune a transformer model for relation prediction, execute the following script. Models, tasks and hyper-parameters can be specified within the script.
```
sh run_train_relations.sh
```
## Data
The experiments in the paper are based on our AbstRCT corpus, which can be found [here](https://gitlab.com/tomaye/abstrct).
For the argument component detection the data has to be in the **CoNLL** format.
Relation classification requires the data to be in a .tsv format. For converting Brat annotation files into .tsv format, see [create_tsv_from_brat.py](/preprocessing/create_tsv_from_brat.py).
