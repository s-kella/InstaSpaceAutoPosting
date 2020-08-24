from PIL import Image
import os
from instabot import Bot
from dotenv import load_dotenv


load_dotenv()
name = os.getenv('NAME')
password = os.getenv('PASSWORD')
bot = Bot()
bot.login(username=name, password=password)

path = os.getcwd()
dir_name = 'images'
path += '\\' + dir_name
os.chdir(path)

files = os.listdir(path)
for file in files:
    image = Image.open(file)
    image.thumbnail((1800, 1800))
    image.save(file, format='JPEG')
    bot.upload_photo(file)
    file += '.REMOVE_ME'
    os.remove(file)
