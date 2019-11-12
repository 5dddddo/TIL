from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.name}'

class Article(models.Model):
    title = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    content = models.TextField()
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.content}'