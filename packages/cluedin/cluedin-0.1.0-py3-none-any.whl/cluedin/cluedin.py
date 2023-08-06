import requests


def get_token_response(username, password, org_name, auth_url):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'username': username,
        'password': password,
        'client_id': org_name,
        'grant_type': 'password'
    }
    response = requests.post(auth_url, headers=headers, data=data)
    return response.json()


def get_token(username, password, org_name, auth_url):
    return get_token_response(username, password, org_name, auth_url)['access_token']
