from typing import Tuple, Optional
from PIL import Image, ImageFont, ImageDraw
import os.path


class ImageTextBox(object):

    def __init__(self, text, width, height, fontfile="impact.ttf",
                 background=(0, 0, 0, 0), font_size=1, align="center", color="black"):
        self.text = text
        if self.text.strip(" ") == "":
            raise NoTextError

        self.height = height
        self.width = width

        self.background = background
        self.font_size = font_size
        self.fontfile = os.path.join(os.path.dirname(__file__), f'fonts/{fontfile}')
        self.align = align
        self.color = color

        self.font = ImageFont.truetype(self.fontfile, self.font_size)

        self.img = Image.new('RGBA', (width, height), background)
        self.imgDraw = ImageDraw.Draw(self.img)

        self.warp_text()
        self.resize_to_fit()

    def load(self):
        self.img.load()

    def save(self, filename):
        self.img.save(filename)

    def get_image(self):
        return self.img

    def warp_text(self):
        """
        >>> text = "Hello  my name  is Caveman "
        >>> img = ImageTextBox(text, 100, 200)
        >>> img.warp_text()
        ['Hello', 'my', 'name', 'is', 'Caveman']

        :return:
        """
        self.text = self.text.strip(" ")
        self.text = self.text.split(" ")
        index = 0
        while index < len(self.text):
            if self.text[index] == '':
                self.text.pop(index)
            else:
                index += 1
        return self.text

    def fit_text(self) -> Optional[Tuple]:
        """
        Takes the text and breaks it down into multiple lines

        :returns: the height of the text

        >>> text = "Hello my name is Caveman"
        >>> img = ImageTextBox(text, 100, 200)
        >>> img.fit_text()
        """
        words = self.text
        lines = []
        temp_index = 0

        lines.append("")

        w = 0
        h = 0

        word_too_big = False
        for word in words:
            w, h = self.imgDraw.textsize(lines[temp_index] + f"{word}", self.font)
            if w >= self.width:
                word_w, word_h = self.imgDraw.textsize(word, self.font)
                # checks if one word is too big
                if word_w >= self.width:
                    word_too_big = True
                    if temp_index == 0 and lines[temp_index] == "":
                        lines[temp_index] = word
                    else:
                        lines.append(f"{word} ")
                else:
                    temp_index += 1
                    lines.append(f"{word} ")
            else:
                lines[temp_index] = lines[temp_index] + f"{word} "

        pos = 0
        for i in lines:
            pos += h

        if word_too_big:
            self.font_size -= 1
            self.font = ImageFont.truetype(self.fontfile, self.font_size)
            w, h = self.imgDraw.textsize(" ", self.font)
            return self.height, lines, h
        else:
            return (pos + h), lines, h

    def resize_to_fit(self):
        """
        Takes the text and breaks it down into multiple lines
        and shrinks the font to fit

        :returns: the height of the text

        >>> text = "d"
        >>> img = ImageTextBox(text, 100, 203)
        >>> img.resize_to_fit()
        >>> img.save("temp.png")
        """

        height, lines, text_height = self.fit_text()
        while height < self.height:
            self.font_size += 1
            self.font = ImageFont.truetype(self.fontfile, self.font_size)
            height, lines, text_height = self.fit_text()

        pos = (self.height - (len(lines)*text_height))/2

        color = {"white": (255, 255, 255), "black": (0, 0, 0)}
        for i in lines:

            i = i.strip(" ")
            w, h = self.imgDraw.textsize(i, self.font)

            if self.align.lower() == "center":
                align_coords = (self.width - w)/2
            elif self.align.lower() == "left":
                align_coords = 0
            elif self.align.lower() == "right":
                align_coords = (self.width-w)
            else:
                raise InvalidAlignType

            self.imgDraw.text((align_coords, pos), i, color[self.color],
                              font=self.font)
            pos += text_height




class NoTextError(Exception):
    """ Raised when there is no text input"""
    pass


class InvalidAlignType(Exception):
    """Rasied when align type does not exist"""
    pass
