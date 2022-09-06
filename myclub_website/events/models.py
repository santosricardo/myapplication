from statistics import mode
from django.db import models
from PIL import Image, ImageFont, ImageDraw

class Event(models.Model):
    description = models.TextField(blank=True)

    def __str__(self):
        return self.description

    my_image = Image.open("static/img/choris.jpg")