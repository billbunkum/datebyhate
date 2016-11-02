from django.db import models

from django.contrib.auth.models import User

#important User info: id, email, name, date
class Film(models.Model):
    title = models.CharField(max_length=300)
    genre = models.CharField(max_length=300)
    director = models.CharField(max_length=300, blank=True)
    imdbID = models.CharField(max_length=300, default="empty")
    plot = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.title

class Interest(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    film = models.ForeignKey(Film)

    def imdbID (self):
        return self.film.imdbID