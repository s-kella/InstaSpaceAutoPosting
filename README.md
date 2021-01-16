# InstaSpaceAutoPosting

- Файл fetch_spacex.py скачивает фотографии с последнего запуска SpaceX.
- Файл fetch_hubble.py скачивает выбранную коллекцию фотографий, сделанных с телескопа Hubble.
- Файл publish.py публикует фотографии в инстаграм. После публикации фото удалятся. 

### Как установить

Создайте .env файл с содержимым
```
IG_NAME=[Имя пользователя инстаграм]
IG_PASSWORD=[Пароль]
```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Пример запуска

Для скачивания фото с последнего запуска SpaceX
```
fetch_spacex.py
```
Для скачивания коллекции wallpaper, сделанной с телескопа Hubble
```
fetch_hubble.py wallpaper
```
Для публикации фото
```
publish.py
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
