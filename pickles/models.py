from django.db import models
from django.contrib.auth.models import User

class Pickle(models.Model):
    name = models.CharField(max_length=256)
    created_date = models.DateTimeField('created date')

class Rating(models.Model):
    pickle = models.ForeignKey(Pickle, on_delete=models.CASCADE)
    rating = models.FloatField(default=1.0) # internally 0 is lowest, 1 is highest
    user = models.BigIntegerField() # Want to keep the ratings even if the user is deleted

class Tag(models.Model):
    tag = models.CharField(max_length=64)

class PickleTag(models.Model):
    pickle = models.ForeignKey(Pickle, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)