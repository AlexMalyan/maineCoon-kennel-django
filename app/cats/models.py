
from django.db import models
from django.urls import reverse


class Cat(models.Model):
    GENDERS = {
        "M": "Кот",
        "F": "Кошка"
    }

    name = models.CharField(max_length=100, verbose_name='Кличка')
    cattery = models.CharField(max_length=255, verbose_name="Питомник")
    color_cats = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Окрас"
    )
    merits = models.CharField(
        max_length=255, verbose_name="Заслуги")  # Заслуги
    gender = models.CharField(
        max_length=1, choices=GENDERS, verbose_name="Пол")
    bitrh = models.DateField(verbose_name="Дата рождения")
    description = models.TextField(verbose_name="Описание")
    mating = models.BooleanField(
        default=True, verbose_name="Вязка")  # Вязка да  = нет
    image = models.ImageField(upload_to='images/', verbose_name="Фото")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("cat", kwargs={"cat_id": self.pk})

    class Meta:
        verbose_name = 'Коты и Кошки'
        verbose_name_plural = 'Коты и Кошки'
