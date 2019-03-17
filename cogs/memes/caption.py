from PIL import Image, ImageFont, ImageDraw, ImageOps
import requests
from io import BytesIO
from cogs.memes.image_box import ImageTextBox
import os.path
import json

with open(os.path.join(os.path.dirname(__file__),"images/images.json")) as f:
    data = json.load(f)

def image_or_text(caption, w, h, font="impact.ttf", align="center"):

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
        img = ImageTextBox(caption, w, h, fontfile=font, align=align)
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
            if "align" in layers[l]:
                layer = image_or_text(caption[index],size[0], size[1],
                                      font=font, align=layers[l]["align"])
            else:
                layer = image_or_text(caption[index], size[0], size[1],
                                      font=font)

            if "rotate" in layers[l]:
                layer = layer.rotate(layers[l]["rotate"], expand=1)

            paste(img, layer, loc)

    img.save(os.path.join(os.path.dirname(__file__), location))
    return True


def all_memes():
    memes = []
    for key in data:
        memes.append(key)

    return memes


def catalog():
    memes = all_memes()

    row_len = 5
    w = int(1080/row_len)

    pich_factor = 300
    wordh_factor = 30

    back_w = int(w*row_len)
    back_h = int((len(memes)/row_len)+1)*(pich_factor + wordh_factor)

    back = Image.new('RGBA', (back_w, back_h), (255, 255, 255, 255))
    font = "Calibri.ttf"
    h = 0

    meme_num = 0
    while meme_num < len(data):
        for col in range(row_len):

            file = data[memes[meme_num]]["file"]
            img = Image.open(os.path.join(os.path.dirname(__file__),
                                          f'images/{file}'))
            img.thumbnail((w, pich_factor))
            loc_x = int((w*col) + ((w - img.width)/2))
            loc_y = int(h + ((pich_factor - img.height) / 2))
            paste(back, img, (loc_x, loc_y))

            des = ImageTextBox(memes[meme_num], w, wordh_factor,
                               fontfile=font)
            des = des.get_image()
            paste(back, des, (loc_x, h + pich_factor))
            meme_num += 1
            if meme_num >= len(data):
                break

        h = h + pich_factor + wordh_factor

    back.save(os.path.join(os.path.dirname(__file__), "../../temp_img/catalog.png"))


# e = ImageTextBox("my name jkadhakjd, wdhjahd , dasdhaid ,as dahkd ald", 100, 200)
# b = e.get_image()
# b.save( "../../temp_img/temp.png")


#b = catalog()
#b.save( "../../temp_img/temp.png")
