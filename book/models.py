from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=64, verbose_name="책명")
    author = models.CharField(max_length=64, verbose_name="저자")
    pubdate = models.DateTimeField(auto_now_add=True)
    imageurl = models.URLField(verbose_name='이미지  주소')
    link = models.URLField(verbose_name="링크")
    desc = models.TextField(verbose_name="요약")


    def __str__(self):
        return f'제목: {self.title} 저자: {self.author}'