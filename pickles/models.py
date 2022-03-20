from django.db import models
from django.contrib.auth.models import User

class Pickle(models.Model):
    name = models.CharField(max_length=256)
    maker = models.CharField(max_length=256)
    created_date = models.DateTimeField('created date', auto_now_add=True)

    def __str__(self):
        return self.name

class Rating(models.Model):
    pickle = models.ForeignKey(Pickle, on_delete=models.CASCADE)
    rating = models.FloatField(default=1.0) # internally 0 is lowest, 1 is highest
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    created_date = models.DateTimeField('created date', auto_now_add=True)

    def __str__(self):
        return str(self.rating)

class Tag(models.Model):
    tag = models.CharField(max_length=64)

    def __str__(self):
        return self.tag

class PickleTag(models.Model):
    pickle = models.ForeignKey(Pickle, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f'Pickle {self.pickle} <-> Tag {self.tag}'

class Review(models.Model):
    review = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    created_date = models.DateTimeField('created date', auto_now_add=True)

    def __str__(self):
        MAX_REVIEW_LENGTH = 32
        return f'{self.review[:MAX_REVIEW_LENGTH]}...' if len(self.review) >= MAX_REVIEW_LENGTH else self.review