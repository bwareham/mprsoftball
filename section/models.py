from django.db import models

class Page(models.Model):
    header = models.CharField(max_length = 50, unique = True)
    
    def __unicode__(self):
        return str(self.header)
    
class Item(models.Model):
    page = models.ForeignKey(Page)
    title = models.CharField(max_length = 50, blank = True)
    content = models.TextField()
    position = models.PositiveSmallIntegerField("Position")
    class Meta:
        ordering = ['position']
        
