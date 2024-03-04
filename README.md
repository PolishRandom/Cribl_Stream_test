# Cribl_Stream_test

Directory contains Python script that downloads dataset CSV from kaggle.com, converts it to JSON format, and then sends it to Splunk HEC on local environment.

To download dataset from Kaggle, you need an authorization token, that will be placed in the main directory of downloaded Python environment from this repository.
To get the token please follow one of the two steps:
1. You can download the token that was generated on my Kaggle account and was sent to Cribl by email.
2. You can register by yourself on [Kaggle.com](https://www.kaggle.com/) and generate your own private token.
Token was not included in this repository due to security breach.

When the token is copied to the Cribl directory, activate the environment by command:
source Cribl/bin/activate
This should download all needed dependecied and packages, you can check them in the requirements.txt file.

Next, launch the Python script:
python main.py
or 
python3 main.py

