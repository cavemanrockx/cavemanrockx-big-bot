from PIL import Image, ImageFont, ImageDraw, ImageOps
import requests
from io import BytesIO


def two_buttons(caption1, caption2):

    img = Image.open("images/Two-Buttons.jpg")
    w, h = img.size
    print(w,h)
    layer1 = Image.new('RGBA', img.size, (0, 0, 128, 0))
    layer1draw = ImageDraw.Draw(layer1)

    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("impact.ttf", 50)

    # draw.text((x, y),"Sample Text",(r,g,b))

    layer1draw.text((w/2, h/2), "Sample Text", (0, 0, 0), font=font)

    #layer1 = layer1.rotate(30, expand=1)

    img.paste(layer1, (0, 0), layer1)

    img.save('temp.jpg')

    #response = requests.get(url)
    #img = Image.open(BytesIO(response.content))



two_buttons("foo", "bar")

