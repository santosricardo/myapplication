from statistics import mode
from django.db import models

class Event(models.Model):
    description = models.TextField(blank=True)

    def __str__(self):
        return self.description