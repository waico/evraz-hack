# Welcome to evraz-hack

Code for evraz hack

# How to Run 

## 1. Fork / Clone repo
- fork to your personal repo 
- clone to you local machine


## 2. Use a virtual environment

Сreate and activate virtual environment
```bash
python3 -m venv venv-evraz
echo "export PYTHONPATH=$PWD" >> venv-evraz/bin/activate
source venv-evraz/bin/activate
```

Install dependencies
```bash
pip install -r requirements.txt
```

Add virtual environment to Jupyter Notebook
```bash
python -m ipykernel install --user --name=venv-evraz
``` 

Run Jupyter Notebook 
```bash
jupyter notebook
```

# Data load
Load data to
```
├── data
│   ├── raw   
```
# Model

Notebook for train model `Base_Model4`


# Demo
[evraz-waico](https://share.streamlit.io/dimas71bit/evraz_gui/main)
# The directory structure
```
├── README.md          <- The top-level README for developers using this project.
│
├── data
│   ├── raw            <- The original, immutable data dump.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── external       <- Data from third party sources.
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is task name SHKPA-XX (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `SHKPA-67-mms-test-LSTM-model-on-all-electrolyses`.
│
├── docs               <- Questions and some other related documentation
│
├── results            <- Intermediate analysis as HTML, PDF, LaTeX, etc.
│
├── .gitignore         <- Avoids uploading data, credentials, outputs, system files etc
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
|
└── src                <- Source code for use in this project.
```
