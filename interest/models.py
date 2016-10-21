from django.db import models

from django.contrib.auth.models import User

#important User info: id, email, name, date

class Interest(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, blank=True)
    film = models.ForeignKey(Film)

class Film(models.model):
#    imdb_id =
#   will use API; request 
    pass