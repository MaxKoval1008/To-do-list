from django.db import models


class Picture(models.Model):
    picture_name = models.CharField(max_length=100)
    picture_img = models.ImageField()

    def __str__(self):
        return self.picture_name
