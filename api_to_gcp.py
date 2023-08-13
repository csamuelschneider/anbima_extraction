import ast
from google.cloud import bigquery
import os

serviceAccount = r'D:/Projects/apache-beam-cassio-bolba/apache-beam-curso-e34e2daef2e7.json'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= serviceAccount
table_id = 'apache-beam-curso.raw_anbima.anbima_fundos'

with open('D:/Projects/anbima_test/fundos.txt', 'r', encoding='UTF8') as f:
    data_str = f.read()

data_dict = ast.literal_eval(data_str)

dados_api = data_dict['content']

key = 'data_encerramento'
for item in range(0, len(dados_api)):
    if key not in dados_api[item]['classes_series_cotas'][0].keys():
        dados_api[item]['classes_series_cotas'][0]['data_encerramento'] = None

client = bigquery.Client()

rows_to_insert = dados_api

errors = client.insert_rows_json(table_id, rows_to_insert)
if errors == []:
    print("New rows have been added.")
else:
    print(f"Encountered errors while inserting rows: {errors}")