from PIL import Image, ImageFont, ImageDraw, ImageOps
import requests
from io import BytesIO
from image_utils import ImageText
from image_box import ImageTextBox


def two_buttons(caption1, caption2, url):

    img = Image.open("images/Two-Buttons.jpg")

    layer1_w = 194
    layer1_h = 90

    layer1 = ImageTextBox(caption1, layer1_w, layer1_h)
    layer1 = layer1.get_image()
    layer1 = layer1.rotate(16.4, expand=1)
    img.paste(layer1, (48, 64), layer1)

    layer2_w = 144
    layer2_h = 77

    layer2 = ImageTextBox(caption2, layer2_w, layer1_h)
    layer2 = layer2.get_image()
    layer2 = layer2.rotate(18, expand=1)
    img.paste(layer2, (241, 34), layer2)

    response = requests.get(url)
    layer3 = Image.open(BytesIO(response.content))
    layer3.resize
    img.paste(layer3, (206, 450, 403, 690), layer3)


    img.save('temp.png')

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

    img.save('temp.png')

    # response = requests.get(url)
    # img = Image.open(BytesIO(response.content))

two_buttons("Working on my project", "Working on leacture handout", "http://icons.iconarchive.com/icons/hopstarter/face-avatars/128/Male-Face-I3-icon.png")

