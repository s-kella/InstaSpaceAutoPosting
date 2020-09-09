import requests
import os
import argparse
import pathlib
import utils


def fetch_hubble_picture(collection_name):
    url = 'http://hubblesite.org/api/v3/'
    payload = {'collection_name': collection_name}
    response = requests.get(f'{url}images', params=payload)
    response.raise_for_status()
    for image_info in response.json():
        image_info_url = f'{url}image/{str(image_info["id"])}'
        response = requests.get(image_info_url)
        response.raise_for_status()
        image_url = f"http:{response.json()['image_files'][1]['file_url']}"
        filename = str(image_info['id']) + os.path.splitext(image_url)[1]
        utils.download_photo(image_url, filename)


def main():
    dir_name = 'images'
    os.makedirs(dir_name, exist_ok=True)
    path = pathlib.Path.cwd() / dir_name
    os.chdir(path)
    parser = argparse.ArgumentParser()
    parser.add_argument('collection',
                        help='For example: "holiday_cards", "wallpaper", "spacecraft", "news", "printshop", "stsci_gallery"')
    args = parser.parse_args()
    fetch_hubble_picture(args.collection)


if __name__ == '__main__':
    main()
