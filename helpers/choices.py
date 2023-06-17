from django.db import models


class DoughTypeChoices(models.TextChoices):
    thin = 'THIN', 'Thin'
    thick = 'THICK', 'Thick'

