from django.db import models
from django.urls import reverse


class Category(models.Model):  # раздел категорий и видов декоративной штукатурки
    name = models.CharField(max_length=250, verbose_name='Вид декоративной штукатурки')

    class Meta:
        verbose_name = 'Вид и категория'
        verbose_name_plural = 'Виды категорий'

    def __str__(self):
        return self.name[:30]

    def get_absolute_url(self):
        return reverse('category', kwargs={'pk': self.pk})


class Type(models.Model):  # Тип декоративной штукатурки
    name = models.CharField(max_length=250, verbose_name='Название "Декоративной штукатурки", "Арт Бетона"')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='types',
        verbose_name='Выбрать категорию'
    )

    class Meta:
        verbose_name = 'Тип декоративной штукатурки и артбетона'
        verbose_name_plural = 'Типы декоративных штукатурок и артбетона'

    def __str__(self):
        return self.name[:30]


class Manufacturer(models.Model):  # Информация о производителях декоративной штукатурки и ее описание
    name = models.CharField(max_length=250, verbose_name='Производитель декоративной штукатурки')
    description = models.TextField(verbose_name='Информация о производителе')


    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.name[:30]


class DecorativePlaster(models.Model):  # Декоративная штукатурка
    name = models.CharField(max_length=250,
                            verbose_name='Вид выполненной работы')  # Название и оглавление декоративной штукатурки
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='decorativeplaster/', verbose_name='Картинка')
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name='decorativeplaster',
        verbose_name='Производитель декоративной штукатурки'
    )

    type = models.ForeignKey(
        Type,
        on_delete=models.SET_NULL,
        null=True,
        related_name='decorativeplaster',
        verbose_name='Вид'
    )

    class Meta:
        verbose_name = 'выполненную работу по декоративной штукатурке или артбетону'
        verbose_name_plural = 'выполненные работы по декоративным штукатуркам и артбетону'

    def __str__(self):
        return self.name[:30]

    def get_absolute_url(self):
        return reverse('decorative_plaster_detail', kwargs={'pk': self.pk})
