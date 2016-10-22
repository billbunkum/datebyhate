from django.db import models

from django.contrib.auth.models import User

#important User info: id, email, name, date
class Film(models.Model):
    title_id = models.CharField(max_length=20)
#   may need to change this from CharField

class Interest(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, blank=True)
    film = models.ForeignKey(Film)
