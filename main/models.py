from django.db import models


class USDRate(models.Model):
	usd = models.CharField('Курс Доллара', max_length=100)
	created = models.DateTimeField('Создано', auto_now_add=True)

	class Meta:
		verbose_name = 'Курс доллара'
		verbose_name_plural = 'Курсы доллара'
