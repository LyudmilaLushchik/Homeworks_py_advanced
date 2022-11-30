import requests


def create_folder(token, folder_path):
    URL = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Content-Type': 'application/json',
            'Authorization': f'OAuth {token}'}
    params = {'path': folder_path}
    response = requests.put(url=URL, headers=headers, params=params)
    return response.status_code