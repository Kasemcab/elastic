import pandas as pd
import json
import requests
from requests.auth import HTTPBasicAuth

url = 'http://localhost:9200/_sql?format=json'
data = {
    "query": "SELECT min(Period) FROM newin WHERE Suppressed is not null"
}
auth = HTTPBasicAuth('elastic', 'changeme')
# api_key = ''
# headers = {
#     'Authorization': f'ApiKey {api_key}',
#     'Content-Type': 'application/json'
# }
response = requests.post(url, json=data, auth=auth, headers={'Content-Type': 'application/json'})

json_data = response.json()
rows = json_data['rows']
df = pd.DataFrame(rows, columns=["Amount"])
df.to_csv('./newfile.csv', index=False)
print(df)