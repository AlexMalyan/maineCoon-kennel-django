from django.db import models


class Cat(models.Model):
    GENDERS = {
        "M": "Кот",
        "F": "Кошка"
    }

    name = models.CharField(max_length=100)
    cattery = models.CharField(max_length=255)
    merits = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDERS)
    bitrh = models.DateField()
    description = models.TextField()
    mating = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/')
