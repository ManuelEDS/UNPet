from django.db import models

# Create your models here.


class Pets(models.Model):
    name = models.CharField(max_length=40)
    race = models.TextField(max_length=20)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name
