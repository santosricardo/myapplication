from operator import concat
from statistics import mode
from django.db import models
from PIL import Image, ImageFont, ImageDraw
from textwrap import wrap

class Event(models.Model):
    description = models.TextField()
    def __init__(self, description):
        self._description = description

    def __str__(self):
        return self._description

    def save_image(self):
        description = str(self._description)
        #description = "No entanto, não podemos esquecer que a revolução dos costumes promove a alavancagem dos conhecimentos estratégicos para atingir a excelência."
        new_description = ""
        for i in wrap(description, width=25):
            new_description += i + "\n"
        my_image = Image.open("/home/ricardo/projetos/estudos/myapplication/myclub_website/events/static/img/choris.png")
        title_font = ImageFont.truetype('/home/ricardo/projetos/estudos/myapplication/myclub_website/events/static/fonts/US101.ttf', 50)
        image_editable = ImageDraw.Draw(my_image)
        image_editable.multiline_text((20,20), new_description, (237, 230, 211), font=title_font)
        my_image.save("/home/ricardo/projetos/estudos/myapplication/myclub_website/events/static/img/choris-1.png")