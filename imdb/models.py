from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Movie(models.Model):
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    stars = models.CharField(max_length=300)
    director = models.CharField(max_length=60)
    description = models.TextField()
    date_published = models.DateTimeField(default=timezone.now)
    image_path = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Review(models.Model):
    rating = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])
    body = models.TextField()
    time = models.DateTimeField(default=timezone.now)
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
