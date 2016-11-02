from django.db import models
from django.utils import timezone

class Post(models.Model): #эта строка определяет нашу модель (объект). models.Model означает, что объект Post является моделью Django
    author = models.ForeignKey('auth.User') #ссылка на другую модель
    title = models.CharField(max_length=200) #текстовое поле с ограничением на количество символов.
    text = models.TextField() # поле для неограниченно длинного текста
    create_date = models.DateField(default=timezone.now()) # дата и время
    publish_field = models.DateField(blank=True, null=True) #
    #comments = models.ForeignObject()

    def publish(self):
        self.publish_field = timezone.now()
        self.save()

    def __srt__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Comment(models.Model):
    post = models.ForeignKey('blog.Post') #related_name option in models.ForeignKey allows us to have access to comments from within the Post model.
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text