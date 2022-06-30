from django.db import models


class Burgers(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    protein = models.CharField(max_length=255, verbose_name='Протейин')
    Carbohydrates = models.CharField(max_length=255, verbose_name='Углеводы')
    colories = models.CharField(max_length=255, verbose_name='свет продукта')
    img = models.ImageField(verbose_name='фото продукта')

    def __str__(self):
        return self.title


class Stuffed_berger(models.Model):
    title = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255)
    desc = models.TextField()
    img = models.ImageField()
