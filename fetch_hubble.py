import requests
import os
import argparse


def download(url, filename):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def find_extension(url):
    url = url.split('.')
    return url[-1]


def fetch_hubble_picture(collection_name):
    url = 'http://hubblesite.org/api/v3/images'
    payload = {'collection_name': collection_name}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for image_info in response.json():
        image_info_url = url.strip('s') + '/' + str(image_info['id'])  # ссылка на инфо и ссылки со всеми размерами
        response = requests.get(image_info_url)
        response.raise_for_status()
        image_url = 'http:' + response.json()["image_files"][1]['file_url']  # ссылка на самую большую картинку
        filename = str(image_info['id']) + '.' + find_extension(image_url)
        download(image_url, filename)


path = os.getcwd()  # получить текующую папку
files = os.listdir(path)  # список всех файлов
dir_name = 'images'
if dir_name not in files:
    os.mkdir(dir_name)  # создать папку
path += '\\' + dir_name
os.chdir(path)  # сменить папку
parser=argparse.ArgumentParser()
parser.add_argument('collection',help='For example: "holiday_cards", "wallpaper", "spacecraft", "news", "printshop", "stsci_gallery"')
args = parser.parse_args()
fetch_hubble_picture(args.collection)
