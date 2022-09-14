from operator import concat
from statistics import mode
from django.db import models
from PIL import Image, ImageFont, ImageDraw
from textwrap import wrap
#from myclub_website.events.views import generate

class Event(models.Model):
    description = models.TextField()
    # def __init__(self):
    #     self._description = description

    def __str__(self):
        return self.description

    def save_image(descricao):
        new_description = ""
        for i in wrap(str(descricao), width=28):
            new_description += i + "\n"
        len_description = len(new_description)
        if len_description < 200:
            my_image = Image.open("/home/ricardo/projetos/estudos/myapplication/myclub_website/events/static/img/choris.png")
            title_font = ImageFont.truetype('/home/ricardo/projetos/estudos/myapplication/myclub_website/events/static/fonts/US101.ttf', 45)
            image_editable = ImageDraw.Draw(my_image)
            image_editable.multiline_text((20,20), new_description, (237, 230, 211), font=title_font)
            my_image.save("/home/ricardo/projetos/estudos/myapplication/myclub_website/events/static/img/choris-quotes.png")
        else:
            new_description = 'Sorry, your citation cannot be generated. There is a limit of 200 characters.'
        return new_description