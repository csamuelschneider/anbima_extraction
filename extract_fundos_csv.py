import requests
import json
import base64
import config

def authenticate(url_token, client_id, client_secret):
    decoded_auth = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {decoded_auth}"
    }
    data = {
        "grant_type": "client_credentials"
    }
    auth_response = requests.post(url_token, headers=headers, json=data).json()
    access_token = auth_response['access_token']
    return access_token 


def apiCall(url_base, client_id, access_token):
    header_token = {
        "Content-Type": "application/json",
        "client_id": client_id,
        "access_token": access_token
    }
    fundos_response = requests.get(url_base, headers=header_token)
    fundos_json = str(fundos_response.json())
    return fundos_json


def dict_to_csv(data, filename):
    with open(filename, 'w', encoding='UTF8') as f:
        f.write(data)
        f.close()


def main():
    url_token = "https://api.anbima.com.br/oauth/access-token"
    url_base = "https://api-sandbox.anbima.com.br/feed/fundos/v1/fundos-estruturados?classe-anbima=FII"

    access_token = authenticate(url_token, config.client_id, config.client_secret)
    fundos_json = apiCall(url_base, config.client_id, access_token)
    path = 'D:/Projects/anbima_test/fundos_csv.csv'
    dict_to_csv(fundos_json, path)

if __name__ == "__main__":
    main()







