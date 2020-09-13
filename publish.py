from PIL import Image
import os
import pathlib
from instabot import Bot
from dotenv import load_dotenv


def main():
    load_dotenv()
    name = os.getenv('IG_NAME')
    password = os.getenv('IG_PASSWORD')
    bot = Bot()
    bot.login(username=name, password=password)

    dir_name = 'images'
    path = pathlib.Path.cwd() / dir_name
    os.chdir(path)

    file_names = os.listdir(path)
    for file_name in file_names:
        image = Image.open(file_name)
        image.thumbnail((1800, 1800))
        image.save(file_name, format='JPEG')
        bot.upload_photo(file_name)


if __name__ == '__main__':
    main()
