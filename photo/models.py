from django.db import models
from rostermaker.models import Player
from filebrowser.fields import FileBrowseField

class Photo(models.Model):
    image = FileBrowseField("Image", max_length=200, directory="uploads/", extensions=[".jpg",".jpeg",".gif"], blank=True, null=True, help_text="Required")
    description = models.CharField(max_length=50, help_text="Short identifier")
    caption = models.TextField(null=True, blank=True, help_text="Optional: Longer description of what's happening in the photo")
    player_tag = models.ManyToManyField(Player, null=True, blank=True, help_text="Optional: Identify players in photo" )
    year = models.PositiveSmallIntegerField(null=True, blank=True, help_text="Optional: Season photo was taken")
    
    def __unicode__(self):
        return self.description