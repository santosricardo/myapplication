from statistics import mode
from django.db import models
from PIL import Image, ImageFont, ImageDraw

class Event(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description

    my_image = Image.open("/home/ricardo/projetos/myapplication/myclub_website/events/static/img/choris.jpg")
    title_font = ImageFont.truetype('/home/ricardo/projetos/myapplication/myclub_website/events/static/fonts/US101.ttf', 200)
    image_editable = ImageDraw.Draw(my_image)
    title_text = "Testando a inserção de texto"
    image_editable.text((15,15), title_text, (237, 230, 211), font=title_font)
    my_image.save("/home/ricardo/projetos/myapplication/myclub_website/events/static/img/result.jpg")