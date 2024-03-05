import opendatasets
import requests
import os
import pandas
import json

# This section downloads dataset from kaggle.com url
url = 'https://www.kaggle.com/datasets/gregorut/videogamesales'
dataset_dir = 'datasets'

opendatasets.download(url, dataset_dir)

# This section is responsible for finding the dataset file 
dataset_name_dir = os.listdir(dataset_dir)[0]
full_dataset_dir_path = os.path.join(dataset_dir, dataset_name_dir)

dataset_file = os.listdir(full_dataset_dir_path)[0]
full_dataset_file_path = os.path.join(full_dataset_dir_path, dataset_file)


# This section converts CSV to JSON
csv_data = pandas.read_csv(full_dataset_file_path)
json_data = csv_data.to_json(orient='records', indent=4)

event_data = {
    'event': 'test event'
}

payload = {
    'jsonData': json.loads(json_data),
    **event_data
}

body = json.dumps(payload, indent=4)


# POST https request
http_url = 'http://localhost:8088/services/collector'

headers = {
#    'Authorization': 'Splunk <token>',
}

response = requests.post(http_url, headers=headers, data=body)

if response.status_code == 200:
    print("Data transfer has been successful.")
else:
    print("Data transfer failed with code:", response.status_code)
    print("Error message:", response.text)
