from django.db import models

# Create your models here.

class UserModel(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=200)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome