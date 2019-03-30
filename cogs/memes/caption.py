from PIL import Image, ImageFont, ImageDraw, ImageOps
import requests
from io import BytesIO
from cogs.memes.image_box import ImageTextBox
import os.path
import json

with open(os.path.join(os.path.dirname(__file__),"images/images.json")) as f:
    data = json.load(f)


def image_or_text(caption, w, h, font="impact.ttf", align="center", color="black"):

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
        img = ImageTextBox(caption, w, h, fontfile=font, align=align, color=color)
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
    for i in range(len(caption)):
        if caption[i].strip(" ") == "":
            caption.pop(i)

    caption_count = 0

    # for the caption count that needs to be accepted
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

        # main block when caption exists

        if caption[index].strip(" ") != "*":
            align = "center"
            color = "black"
            if "align" in layers[l]:
                align = layers[l]["align"]

            if "color" in layers[l]:
                color = layers[l]["color"]

            layer = image_or_text(caption[index], size[0], size[1],
                                  font=font, align=align, color=color)
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

    row_len = 6
    w = int(1080/row_len)

    pich_factor = 300
    wordh_factor = 30

    border_width = 8

    back_w = int(w*row_len) + (border_width*(row_len+1))

    if len(memes)/row_len == 0:
        bach_h_size = int(len(memes)/row_len)
    else:
        bach_h_size = int(len(memes)/row_len) + 1

    back_h = bach_h_size * (pich_factor + wordh_factor + border_width)
    back_h += border_width

    back = Image.new('RGBA', (back_w, back_h), (131, 131, 131, 255))
    font = "Calibri.ttf"

    border_x = Image.new('RGBA', (back_w, border_width), (0, 0, 0, 255))
    border_y = Image.new('RGBA', (border_width, back_h), (0, 0, 0, 255))
    h = 0

    meme_num = 0
    while meme_num < len(data):
        paste(back, border_x, (0, h))
        h += border_width
        for col in range(row_len):

            # Image
            file = data[memes[meme_num]]["file"]
            img = Image.open(os.path.join(os.path.dirname(__file__),
                                          f'images/{file}'))
            img.thumbnail((w, pich_factor))
            loc_x = int((w*col) + (w - img.width)/2)
            loc_x += border_width*(col + 1)
            loc_y = int(h + ((pich_factor - img.height) / 2))
            paste(back, img, (loc_x, loc_y))

            # Text
            des = ImageTextBox(memes[meme_num], w, wordh_factor,
                               fontfile=font)
            des = des.get_image()
            paste(back, des, (loc_x, h + pich_factor))
            meme_num += 1

            if meme_num >= len(data):
                break

        h = h + pich_factor + wordh_factor

    paste(back, border_x, (border_width, h))

    loc = 0
    for x in range(row_len + 1):
        paste(back, border_y, (loc, 0))
        loc += (border_width + w)

    back.save(os.path.join(os.path.dirname(__file__), "../../temp_img/catalog.png"))


def seal(url, location):
    seal = Image.open(os.path.join(os.path.dirname(__file__), "images/seal.png"))

    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
    except:
        return False

    seal.thumbnail((img.width*0.35, img.height*0.2))
    x = img.width - seal.width - 10
    y = img.height - seal.height - 10
    paste(img, seal, (x, y))

    img.save(os.path.join(os.path.dirname(__file__), location))
    return True

# e = ImageTextBox("my name jkadhakjd, wdhjahd , dasdhaid ,as dahkd ald", 100, 200)
# b = e.get_image()
# b.save( "../../temp_img/temp.png")


# b = catalog()
# b.save( "../../temp_img/temp.png")
