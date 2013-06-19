from django.db import models
from rostermaker.models import Player
from django import forms

class Season(models.Model):
    year = models.IntegerField(unique = True, max_length=4, verbose_name = "Season (year)")
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
        
class season_choice(forms.Form):
    choice = forms.ModelChoiceField(queryset=Season.objects.all().order_by('year'), empty_label='Go to season page', to_field_name='year', label='', widget=forms.Select(attrs={"onChange":'this.form.submit();'}))

class player_choice(forms.Form):
    choice = forms.ModelChoiceField(queryset=Player.objects.all().order_by('lastName', 'firstName'), empty_label='Go to player page', to_field_name='pk', label='', widget=forms.Select(attrs={"onChange":'this.form.submit();'}))
    
    
class Quicklink(forms.Form):
    season_link = forms.ModelChoiceField(queryset=Season.objects.all().order_by('year'), empty_label='Choose season', to_field_name='year', label='Quicklink to season page:', widget=forms.Select(attrs={"onChange":'this.form.submit();'}))
    player_link = forms.ModelChoiceField(queryset=Player.objects.all().order_by('lastName','firstName'), empty_label='Choose player', to_field_name='pk', label='Quicklink to player page:', widget=forms.Select(attrs={"onChange":'this.form.submit();'}))