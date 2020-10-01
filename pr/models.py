from django.db import models
# from django.urls import reverse
# import numpy as np
from django.db.models import Avg



class Company(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey( 'auth.User', on_delete=models.CASCADE, ) 
    image = models.ImageField(upload_to='companies/%Y/%m/%d', blank=True)
    body = models.TextField()

    # def get_absolute_url(self):
    #     return reverse ('company_detail', args=[self.pk])
    
    # def average_rating(self):
    #     all_ratings = map(lambda x: x.rating, self.review_set.all())
    #     return np.mean(all_ratings)

    def average_rating(self):
        return self.review_set.aggregate(Avg('rating'))['rating__avg']
        
    def __str__(self):
        return self.name


class Review(models.Model):
    RATING_CHOICES = (
        (1, 'Terrible'),
        (2, 'Poor'),
        (3, 'Average'), 
        (4, 'Very Good'), 
        (5, 'Excellent'),
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)