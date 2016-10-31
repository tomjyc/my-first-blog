from django.db import models
from django.utils import timezone

class Post(models.Model): #эта строка определяет нашу модель (объект). models.Model означает, что объект Post является моделью Django
    author = models.ForeignKey('auth.User') #ссылка на другую модель
    title = models.CharField(max_length=200) #текстовое поле с ограничением на количество символов.
    text = models.TextField() # поле для неограниченно длинного текста
    create_date = models.DateField(default=timezone.now()) # дата и время
    publish_field = models.DateField(blank=True, null=True) #

    def publish(self):
        self.publishd_date = timezone.now()
        self.save()

    def __srt__(self):
        return self.title
