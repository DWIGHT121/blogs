from django.db import models

# Create your models here.
class Articles(models.Model):
    topic = models.CharField(max_length = 200)
    start_text = models.TextField(null = True)
    field1 = models.TextField(max_length = 50000)
    field2 = models.TextField(max_length = 50000)
    image = models.ImageField(upload_to = '', default = 'media/noimg2.png')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.topic

class ArticlesImage(models.Model):
    article = models.ForeignKey(Articles, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = '')

    def __str__(self):
        return self.article.topic


