from datetime import datetime
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

CHOICES_SERVICES = (
    ('Разработка веб сайтов', 'Разработка веб сайтов'),
    ('Разработка мобильных приложений', 'Разработка мобильных приложений'),
    ('Разработка DescTopApp', 'Разработка DescTopApp'),
)


class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name='Напишите название услуги')
    description = models.TextField(verbose_name='Напишите описание услуги')
    choices_services = models.CharField(max_length=100, choices=CHOICES_SERVICES,
                                        verbose_name='Выберите категорию услуг')
    prepaid_expense = models.PositiveIntegerField(validators=[MinValueValidator(1000),
                                                              MaxValueValidator(3000)],
                                                  verbose_name='Внесите аванс', default=1500)
    card_number = models.CharField(max_length=16, verbose_name='Напишите номер карты')
    card_month = models.PositiveIntegerField(null=True,
                                             verbose_name='Укажите месяц', default=1)
    card_year = models.PositiveIntegerField(null=True,
                                            verbose_name='Укажите год', default=2000)
    card_cvv = models.CharField(max_length=3, verbose_name='Укажите cvv')
    email = models.EmailField(verbose_name='Укажите почту', default='@gmail.com')
    dead_line = models.DateTimeField(verbose_name='Укажите дедлайн', default=datetime.now())

    def __str__(self):
        return f'{self.title} - {self.dead_line}'

