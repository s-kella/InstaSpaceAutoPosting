import requests
import os


def download(url, filename):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def find_extension(url):
    url = url.split('.')
    return url[-1]


def fetch_spacex_last_launch():
    url = 'http://api.spacexdata.com/v3/launches/latest'  # откуда беру ссылки на фото
    response = requests.get(url)
    response.raise_for_status()
    for image_number, image_url in enumerate(response.json()['links']['flickr_images']):
        filename = 'spacex' + str(image_number + 1) + '.jpg'
        download(image_url, filename)


path = os.getcwd()
files = os.listdir(path)
dir_name = 'images'
if dir_name not in files:
    os.mkdir(path)
path += '\\' + dir_name
os.chdir(path)
fetch_spacex_last_launch()
