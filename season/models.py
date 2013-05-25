from django.db import models
from rostermaker.models import Player

class Season(models.Model):
    year = models.IntegerField(unique = True, verbose_name = "Season (year)")
    wins = models.IntegerField(blank = True)
    losses = models.IntegerField(blank = True)
    ties = models.IntegerField(blank = True, null = True)
    recap = models.TextField(verbose_name = "Season in Review", blank = True)
    roster = models.ManyToManyField(Player, blank = True, verbose_name = "Roster", related_name = 'roster')
    captains = models.ManyToManyField(Player, blank = True, verbose_name = "Captains", related_name = 'captains')
    rookies = models.ManyToManyField(Player, blank = True, verbose_name = "Rookie(s) of the Year", related_name = 'rookies')
    mvp = models.ManyToManyField(Player, blank = True, verbose_name = "Most Valuable Player(s)", related_name = 'mvp')
    battingchamps = models.ManyToManyField(Player, blank = True, verbose_name = "Batting Champs", related_name = 'battingchamps')
    goldengloves = models.ManyToManyField(Player, blank = True, verbose_name = "Golden Glove(s)", related_name = 'goldengloves')
    mostimproved = models.ManyToManyField(Player, blank = True, verbose_name = "Most Improved", related_name = 'mostimproved')
    whippet = models.ManyToManyField(Player, blank = True, verbose_name = "Whippet(s) of the Year", related_name = 'whippet')
    bombat = models.ManyToManyField(Player, blank = True, verbose_name = "Bombat Winner", related_name = 'bombat')
    walker = models.ManyToManyField(Player, blank = True, verbose_name = "Walker Award", related_name = 'walker')
    
    
    def __unicode__(self):
        return str(self.year)
        