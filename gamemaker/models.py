from django.db import models
from django.forms import ModelForm
from time import strftime
from rostermaker.models import Player
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db.models.loading import cache as model_cache


def PlayedGames():
    games = Game.objects.filter(when__year=timezone.now().year, when__lte=timezone.now()).order_by('-when')
    return games

def LatestGames():
    games = Game.objects.filter(when__gte=timezone.now()).order_by('when')
    return games


class Game(models.Model):
    when = models.DateTimeField(unique = True)
    opponent = models.CharField(max_length = 50, default="TBD")
    location = models.CharField(max_length = 50)
    RosterRulesOn = models.BooleanField('Roster rules', default = 'True', help_text = "Roster size and gender ratio rules will be enforced when checked")
    players = models.ManyToManyField(Player, limit_choices_to={'id__in': Player.objects.filter(active='True')}, null=True, blank=True )
    scoreMPR = models.IntegerField(max_length = 2, verbose_name = "MPR", null=True, blank=True,)
    scoreOPP = models.IntegerField(max_length = 2, verbose_name = "Opponent", null=True, blank=True,)


    #objects = models.Manager()
    #latest_games = LatestGamesList()
    #played_games = PlayedGamesList()

    def __unicode__(self):
        when = timezone.localtime(self.when)
        return when.strftime('%a, %b %d, %Y %I:%M %p')
    
class Stat(models.Model):
    g = models.ForeignKey(Game, related_name = 'statgame')
    player = models.ForeignKey(Player, related_name = 'statplayer', limit_choices_to={'active': True})
    AB = models.PositiveSmallIntegerField()
    single = models.PositiveSmallIntegerField(null=True, blank=True)
    double = models.PositiveSmallIntegerField(null=True, blank=True)
    triple = models.PositiveSmallIntegerField(null=True, blank=True)
    HR = models.PositiveSmallIntegerField(null=True, blank=True)
    SAC = models.PositiveSmallIntegerField(null=True, blank=True)
    BB = models.PositiveSmallIntegerField(null=True, blank=True)
    SO = models.PositiveSmallIntegerField(null=True, blank=True)
    R = models.PositiveSmallIntegerField(null=True, blank=True)
    RBI = models.PositiveSmallIntegerField(null=True, blank=True)    
    
class GameRosterForm(ModelForm):
    class Meta:
        model = Game

    def clean(self):
        super(GameRosterForm, self).clean()
        players = self.cleaned_data.get('players', None)
        RosterRulesOn = self.cleaned_data.get('RosterRulesOn', None)
        women = [player for player in players if player.sex=='F']
        women_count = len(women)
        total = len(players)
        if total != 0:
            womenPct = int((len(women)/float(total))*100)
        else:
            womenPct = 0
        if RosterRulesOn is True and total != 0 and total < 8:
            raise ValidationError('Rosters must have at least 8 players. You have only selected %s.' % total) 
        if RosterRulesOn is True and total > 18:
            raise ValidationError('Rosters cannot have more than 18 players. You have selected %s.' % total)
        if RosterRulesOn is True and total != 0 and womenPct < 40:
            raise ValidationError('Women must make up at least 40 percent of roster. They only constitute %s percent now.' % (womenPct))   
        return self.cleaned_data
        
