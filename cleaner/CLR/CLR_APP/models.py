from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Введите жанр",
                            verbose_name="Жанр")
    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=20,
                            help_text="Введите язык")
    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=100,help_text='Введите имя автора', verbose_name='Имя автора')
    last_name = models.CharField(max_length=100, help_text="Введите фамилию автора", verbose_name='Фамилия автора')
    date_of_birth = models.DateField(help_text='Введите дату рождения', verbose_name='Дата рождения', null=True, blank=True)
    about = models.TextField(help_text='Введите сведения об авторе', verbose_name='Сведения об авторе')
    # photo = models.ImageField(upload_to='images', help_text='Введите фото автора',verbose_name='Фото автора', null=True,blank=True)

    def __str__(self) :
        return self.last_name

class App(models.Model):
    name_App = models.CharField(max_length=200,help_text='Введите название приложения', verbose_name='Название приложения')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, help_text="Выберите жанр для приложения", verbose_name='Жанр', null=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE, help_text='Выберите язык', verbose_name='Язык', null=True)
    date_of_out = models.CharField(max_length=4,
                            help_text="Введите год выхода",
                            verbose_name="Год выхода")
    author = models.ManyToManyField('Author', help_text='Выберите создателей ', verbose_name='Создатели приложения', null=True)
    summary = models.TextField(max_length=1000, help_text='Введите краткое содержание приложения', verbose_name='Описание приложения')
    price = models.DecimalField(decimal_places=2, max_digits=7,help_text='Введите цену', verbose_name='Цена (руб.)')
    photo = models.ImageField(upload_to='images',
                              help_text='Введите изображение приложения',
                              verbose_name="Изображение")
    def __str__(self):
        return self.name_App
