from django.db import models

# Create your models here.

class Fighters(models.Model):
    first_name = models.CharField(max_length=200)
    moniker = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    reach = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    age = models.IntegerField(default=0, blank=True)
    opponent = models.ForeignKey('Fighters', related_name='against', on_delete='CASCADE') 
    win = models.BooleanField(default=False, blank=True, verbose_name="win?")
    ko_percent = models.IntegerField(default=0)
    sub_percent = models.IntegerField(default=0)
    dec_percent = models.IntegerField(default=0)
    date_create = models.DateField(auto_now_add=True, null=True)
    date_last_modified = models.DateTimeField(auto_now=True, editable=True)

    def __str__(self):
        return self.first_name + ' "' + self.moniker + '" ' + self.last_name
