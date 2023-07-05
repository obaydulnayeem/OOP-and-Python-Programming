"""  
Download and change desktop wallpaper autometically
"""
import requests # library download command: pip install requests
import json
import PyWallpaper

api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
# api_url = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY"

# get the json
response = requests.get(api_url)
content = response.content.decode('UTF-8')

# convert string to json
dict_content = json.loads(content)

# get the image url
image_url = dict_content['url']

# download the image
res = requests.get(image_url) 

# save the image 
with open('apod.png', 'wb') as image:
    image.write(res.content)

# set as wallpaper
PyWallpaper.change_wallpaper('E:\Programming\OOP-and-Python-Programming\02_OOP\07_Projects\13_Auto Wallpaper\apod.png')