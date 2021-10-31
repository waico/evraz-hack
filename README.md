# Welcome to evraz-hack

Code for evraz hack
Contacts: tg - @_iv_maksimov
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

Notebook for train final model `FinalSubmission`

# Description task 1

1. Собрали все данные по плавкам. Некоторые данные агрегировали по среднему, некоторые по сумме значений (интегралу) и медиане. Выделили отдельные значения на конец продувки (температуры металла).
2. По газу сделали агрегации по данным начала и конца продувки. По ним сделали отдельные агрегации.
3. Отбросили малозначимые признаки
4. Сформировали датасет.
5. Подробный код в  `FinalSubmission.ipynb`

# Description task 2

1. Задача прогноза температуры и концентрации углерода в моменте. 
Демо: [evraz.waico.ru](https://share.streamlit.io/dimas71bit/evraz_gui/main)
Получем данные из АСУТП и в реальном масштабе времени прогнозируем текущие показатели температуры и углерода, что позволяет принимать решение о продоожении или завершении продувки. Целевое решение предполагает на основании этих данных прогнозирование параметров до целевых значений.
1. Построили линейную модель для прогноза температуры расплава и концентрации углерода для решения обратной задачи создания системы поддержки принятия решений и рекомендаций машинисту необходимых параметров (`Notebooks/LassoCV.ipynb`). В рамках данной модели возможно давать рекомендации машинисту по ведению технологического процесса.


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
