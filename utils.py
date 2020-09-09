import requests

def download_photo(url, filename):
    response = requests.get(url, verify=False)  # получить ответ сайта в переменную response
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)