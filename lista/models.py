from django.db import models

class Item(models.Model):
    item = models.CharField(max_length=200)
    quantidade = models.IntegerField(default=0)
    preco = models.FloatField(default=0, null=True)

    def __str__(self):
        return self.item
# Create your models here.
