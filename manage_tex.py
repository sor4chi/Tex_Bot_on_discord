import requests
from PIL import Image

def get_tex_image(code, filename):
    url=f'https://chart.googleapis.com/chart?cht=tx&chl={code}'
    urlData = requests.get(url).content
    with open(f'./data/{filename}.png' ,mode='wb') as f:
        f.write(urlData)

def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result