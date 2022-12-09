from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self) -> str:
        return str(self.name)


class Course(models.Model):
    title = models.CharField(max_length=200, unique=True, null=False)
    about = models.TextField(max_length=200, null=False)
    content = models.TextField(max_length=1024, null=False)
    photo = models.FileField(upload_to='photo/', null=True)
    price = models.FloatField(null=False, default=1)
    

    def __str__(self) -> str:
        return str(self.title)
