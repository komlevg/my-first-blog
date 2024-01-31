from django.db import models
from django.urls import reverse

# Create your models here.
class SkyNews(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")#строковое поле с ограничением кол-ва ввода
    slug = models.SlugField(max_length=255, db_index=True, unique=True)
    newscontent = models.TextField(blank=True)#бланк тру - можно ниче не передавать
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})