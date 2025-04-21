# blog/models.py
from django.db import models
# Create your models here
class RankingBoard(models.Model):          # add the Post table to the DB
    namechar = models.CharField(max_length=200)
    datetime = models.DateTimeField(auto_now_add=True)
    mark = models.IntegerField(default=0)
    def __str__(self):                     # add this __str__ function with DOUBLE underscore
        return self.namechar
