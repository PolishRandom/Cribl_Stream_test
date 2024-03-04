# Cribl_Stream_test

Repository contains Python environment with script, that downloads dataset CSV from kaggle.com, converts it to JSON format, and then sends it to Splunk HEC on local environment.
Please download the cribl_project.tar.gz file and unpack it in the preferred directory, you can use below command in the terminal:
 -  tar -xvzf cribl_project.tar.gz

Prerequisites

To download dataset from Kaggle, you need an authorization token, that will be placed in the main directory of downloaded Python environment from this repository.
To get the token please follow one of the two steps:
1. You can download the token that was generated on my Kaggle account and was sent to Cribl by email.
2. You can register by yourself on [Kaggle.com](https://www.kaggle.com/) and generate your own private token.

Token was not included in this repository due to possible security breach.
When the token is copied to the main cribl_project directory, proceed to the next steps.

This project is created as environment, to activate it, you need to have venv module installed.
To download the module use the command:
 -  pip install venv

Next, activate the environment by command:
 -  source cribl_project/bin/activate
  
When environment is activated, install modules that are needed for this project (you can check them by opening requirements.txt file):
 -  pip install -r requirements.txt

Next, launch the Python script:
 -  python main.py
   
or 

 -  python3 main.py
