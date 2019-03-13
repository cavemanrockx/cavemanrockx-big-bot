from PIL import Image, ImageFont, ImageDraw, ImageOps
import requests
from io import BytesIO
from cogs.memes.image_box import ImageTextBox
import os.path
import json

with open(os.path.join(os.path.dirname(__file__),"images/images.json")) as f:
    data = json.load(f)

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


def meme(meme_name, caption, location):

    if meme_name in data:
        layers = data[meme_name]["layers"]
        file_loc = f"images/" + str(data[meme_name]["file"])
        font = data[meme_name]["font"]
    else:
        return False

    caption = caption.split(",")
    caption_count = 0

    for l in layers:
        if "use_caption" not in layers[l]:
            caption_count += 1

    if len(caption) < caption_count:
        caption = data[meme_name]["default"].split(",")

    img = Image.open(os.path.join(os.path.dirname(__file__), file_loc))

    caption_num = 0
    for l in layers:
        if "use_caption" in layers[l]:
            index = layers[l]["use_caption"] - 1
        else:
            caption_num += 1
            index = caption_num - 1

        size = layers[l]["size"]
        loc = layers[l]["location"]
        if caption[index] != "*":
            layer = image_or_text(caption[index],
                                  size[0], size[1], font=font)

            if "rotate" in layers[l]:
                layer = layer.rotate(layers[l]["rotate"], expand=1)

            paste(img, layer, loc)

    img.save(os.path.join(os.path.dirname(__file__), location))
    return True


def all_memes():
    memes = ""
    for key in data:
        memes += f"{key} "

    memes = memes.strip(" ")
    memes = memes.replace(" ", ",")

    return memes

#
# e = ImageTextBox("my name jkadhakjd, wdhjahd , dasdhaid ,as dahkd ald", 100, 200)
# b = e.get_image()
# b.save( "../../temp_img/temp.png")
