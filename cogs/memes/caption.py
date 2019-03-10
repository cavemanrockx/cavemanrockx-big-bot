from PIL import Image, ImageFont, ImageDraw, ImageOps
import requests
from io import BytesIO
from cogs.memes.image_box import ImageTextBox
import os.path


def image_or_text(caption, w, h, font="impact.ttf"):

    try:
        response = requests.get(caption)
        img = Image.open(BytesIO(response.content))

        back = Image.new('RGBA', (w, h), (0, 0, 0, 0))

        if img.width > w or img.height > h:
            img.thumbnail((w, h))
            paste(back, img, (int((w - img.width) / 2), int((h - img.height) / 2)))
            img = back
        else:
            img = img.resize((w, h))

    except:
        img = ImageTextBox(caption, w, h, fontfile=font)
        img = img.get_image()

    return img


def paste(img, layer, loc):
    try:
        img.paste(layer, loc, layer)
    except:
        img.paste(layer, loc)


def two_buttons(caption1, caption2, caption3, location):

    img = Image.open(os.path.join(os.path.dirname(__file__), "images/Two-Buttons.jpg"))

    # ========LAYER 1===========
    layer1_w = 194
    layer1_h = 90

    layer1 = image_or_text(caption1, layer1_w, layer1_h)
    layer1 = layer1.rotate(16.4, expand=1)

    layer1_loc = (48, 64)

    paste(img, layer1, layer1_loc)

    # ========LAYER 2===========
    layer2_w = 144
    layer2_h = 77

    layer2 = image_or_text(caption2, layer2_w, layer2_h)
    layer2 = layer2.rotate(17, expand=1)

    layer2_loc = (244, 40)

    paste(img, layer2, layer2_loc)

    # ========LAYER 3===========
    layer3_size = (158, 177)
    layer3 = image_or_text(caption3, layer3_size[0], layer3_size[1])

    layer3_loc = (206, 480)

    paste(img, layer3, layer3_loc)

    # ==========================
    img.save(os.path.join(os.path.dirname(__file__), location))


def talk_idiot(caption1, location):

    img = Image.open(os.path.join(os.path.dirname(__file__), "images/Talk-Idiot.jpg"))

    # ========LAYER 1===========
    layer1_w = 308
    layer1_h = 78

    layer1 = image_or_text(caption1, layer1_w, layer1_h, font="digistrip.ttf")

    layer1_loc = (20, 420)

    paste(img, layer1, layer1_loc)

    # ==========================
    img.save(os.path.join(os.path.dirname(__file__), location))


def vr(caption1, location):

    img = Image.open(os.path.join(os.path.dirname(__file__), "images/vr.jpg"))

    # ========LAYER 1===========
    layer1_w = 173
    layer1_h = 59

    layer1 = image_or_text(caption1, layer1_w, layer1_h)

    layer1_loc = (39, 335)

    paste(img, layer1, layer1_loc)

    # ==========================
    img.save(os.path.join(os.path.dirname(__file__), location))

