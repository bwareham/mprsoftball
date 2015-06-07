from django.db import models

class Weather(models.Model):
	current_time = models.DateTimeField()
	current_icon = models.CharField(max_length=30)
	temp = models.IntegerField()
	skies = models.CharField(max_length=30)
	wind = models.CharField(max_length=30)
	current_forecast = models.CharField(max_length=300)
	fcst1_time = models.DateTimeField()
	fcst1_icon = models.CharField(max_length=30)
	fcst1 = models.CharField(max_length=300)
	fcst2_time = models.DateTimeField()
	fcst2_icon = models.CharField(max_length=30)
	fcst2 = models.CharField(max_length=300)
	fcst3_time = models.DateTimeField()
	fcst3_icon = models.CharField(max_length=30)
	fcst3 = models.CharField(max_length=300)
	fcst4_time = models.DateTimeField()
	fcst4_icon = models.CharField(max_length=30)
	fcst4 = models.CharField(max_length=300)
	fcst5_time = models.DateTimeField()
	fcst5_icon = models.CharField(max_length=30)
	fcst5 = models.CharField(max_length=300)

	def __unicode__(self):
		return self.current_time.strftime('%A %b %d')
