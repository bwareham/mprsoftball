from django.db import models
from rostermaker.models import Player

class HOF(models.Model):
    WING_CHOICES = (
		('MN', 'Main Hall'),
		('SP', 'Satchel Paige Wing'),
		('WP', 'Wally Pipp Ward'),
		('TW', 'Ted Williams Suite'),
	)
    player =  models.ForeignKey(Player)
    wing =  models.CharField(choices = WING_CHOICES, max_length = 2, verbose_name = "Wings and Wards", null=True, blank=True)
    yearEntered =  models.PositiveSmallIntegerField(max_length = 4, verbose_name = "Year Entered")
    inscription =  models.TextField(null=True, blank=True)
    
    def __unicode__(self):
        return str(self.player.lastName + ", " + self.player.firstName + "/" + self.wing)