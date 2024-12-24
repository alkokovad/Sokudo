from django.db import models


class Meet(models.Model):
    start_spot = models.CharField("Начало спота", max_length=500)
    end_spot = models.CharField("Конец спота", max_length=500)
    service_zone = models.CharField("Сервис-зона", max_length=500)

    class Meta:
        verbose_name = 'Сходка'
        verbose_name_plural = 'Сходки'

    def __str__(self):
        return "История сходок"