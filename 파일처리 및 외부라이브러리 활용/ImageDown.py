import requests
from PIL import Image

url = 'http://bit.ly/3ZZyeXQ'
r = requests.get(url, stream=True).raw

img = Image.open(r)
img.show()
img.save('src.png')

print(img.get_format_mimetype)