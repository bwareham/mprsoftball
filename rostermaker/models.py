from django.db import models
from datetime import date
from django.forms import ModelForm
from django.core.exceptions import ValidationError


class Player(models.Model):
    firstName = models.CharField(max_length=50, verbose_name="First Name")
    lastName = models.CharField(max_length=50, verbose_name="Last Name")
    alias = models.CharField(max_length=50, blank=True, help_text = "Any maiden/married names or other aliases a player may have used, separated by commas.")    
    sex_choices = (
        ('M','Male'),
        ('F','Female'),
    )
    sex = models.CharField(max_length=1, choices=sex_choices)
    active = models.BooleanField()
    
    def __unicode__(self):
        return str(self.lastName + ", " + self.firstName)

    class Meta:
        unique_together = ('lastName','firstName')
        ordering = ['lastName','firstName']


class HOF(models.Model):
    WING_CHOICES = (
		('MN', 'Main Hall'),
		('SP', 'Satchel Paige Wing'),
		('WP', 'Wally Pipp Ward'),
	)
    player =  models.ForeignKey(Player, related_name = 'Hall of Fame')
    wing =  models.CharField(choices = WING_CHOICES, max_length = 2, verbose_name = "Wings and Wards", null=True, blank=True)
    yearEntered =  models.PositiveSmallIntegerField(max_length = 4, verbose_name = "Year Entered")
    inscription =  models.TextField(null=True, blank=True)
        

