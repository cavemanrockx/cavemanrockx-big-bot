from PIL import Image, ImageFont, ImageDraw, ImageOps
import requests
from io import BytesIO
from image_utils import ImageText

def two_buttons(caption1, caption2):

    img = Image.open("images/Two-Buttons.jpg")

    layer1_w = 187
    layer1_h = 88
    layer1 = Image.new('RGBA', (layer1_w, layer1_h), (0, 0, 0, 100))
    layer1draw = ImageDraw.Draw(layer1)
    caption1_fs = 500
    # font = ImageFont.truetype(<font-file>, <font-size>)

    layer1_font = ImageFont.truetype("impact.ttf", caption1_fs)

    # draw.text((x, y),"Sample Text",(r,g,b))

    l1w, l1h = layer1draw.multiline_textsize(caption1, layer1_font)

    while (l1w > layer1_w) or (l1h > layer1_h):
        caption1_fs -= 10
        if caption1_fs <= 10:
            caption1_fs = 10
        layer1_font = ImageFont.truetype("impact.ttf", caption1_fs)
        l1w, l1h = layer1draw.multiline_textsize(caption1, layer1_font)


    # layer1draw.text((0, 0), caption1, (0, 0, 0), font=font)

    layer1draw.multiline_text((0, 0), caption1, (0, 0, 0), font=layer1_font, align="center")

    layer1 = layer1.rotate(16.4, expand=1)

    img.paste(layer1, (48, 64), layer1)

    img.save('temp.jpg')

    # response = requests.get(url)
    # img = Image.open(BytesIO(response.content))

def two_buttons2(caption1, caption2):

    img = Image.open("images/Two-Buttons.jpg")

    layer1_w = 187
    layer1_h = 88
    layer1 = ImageText((layer1_w, layer1_h), background=(0, 0, 0, 200))

    #layer1.write_text_box(0, 0, caption1, box_width=layer1_w, color=(0, 0, 0),
                          #font_filename="impact.tff", place="center")
    #layer1.write_text_box(300, 275, caption1, box_width=200, font_filename="impact.ttf",
                          #font_size=15, color=(0, 0, 0), place='justify')

    img.paste(layer1, (48, 64, 100, 325), layer1)

    img.save('temp.jpg')

    # response = requests.get(url)
    # img = Image.open(BytesIO(response.content))

two_buttons("foo", "bar")

