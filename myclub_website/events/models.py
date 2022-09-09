from operator import concat
from statistics import mode
from django.db import models
from PIL import Image, ImageFont, ImageDraw

class Event(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description

    def save_image():
        #title_text = str(self.description)
        title_text = "TIKPRAUtikpren1234567891012345678920123456789301JABEUAHEUAE"
        new_text = ""
        n = int(len(title_text))

        for i in title_text:
            new_text += i
            if(int(len(new_text)) == 30)
                new = '\n'.join(new_text)
        print(new)
        my_image = Image.open("/home/ricardo/projetos/estudos/myapplication/myclub_website/events/static/img/choris.png")
        title_font = ImageFont.truetype('/home/ricardo/projetos/estudos/myapplication/myclub_website/events/static/fonts/US101.ttf', 40)
        image_editable = ImageDraw.Draw(my_image)
        image_editable.multiline_text((20,20), title_text, (237, 230, 211), font=title_font)
        my_image.save("/home/ricardo/projetos/estudos/myapplication/myclub_website/events/static/img/choris-1.png")