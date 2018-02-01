from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Bread(models.Model):
    name = models.CharField(max_length=20)
    level = models.IntegerField(default=1, null=False)
    owner = models.ForeignKey(User, related_name='breads', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} of {}'.format(self.name,self.owner)