from django.db import models

# Create your models here.
class Contenido(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    phone = models.TextField()
    last_name = models.TextField()
    age = models.IntegerField()
    email = models.TextField()
