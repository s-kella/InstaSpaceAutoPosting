import requests
import os
import pathlib
import utils


def fetch_spacex_last_launch():
    url = 'http://api.spacexdata.com/v3/launches/latest'
    response = requests.get(url)
    response.raise_for_status()
    for image_number, image_url in enumerate(response.json()['links']['flickr_images']):
        filename = f'spacex{str(image_number + 1)}.jpg'
        utils.download_photo(image_url, filename)


def main():
    dir_name = 'images'
    os.makedirs(dir_name, exist_ok=True)
    path = pathlib.Path.cwd() / dir_name
    os.chdir(path)
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
