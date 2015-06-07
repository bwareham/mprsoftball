from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from weathergrab.models import Weather
import forecastio
import datetime

#THIS MANAGEMENT COMMAND CALLS WEATHER INFO FROM FORECAST.IO.
#BY SETTING IT TO RUN VIA CRONTAB I LIMIT THE NUMBER OF CALLS USING MY API

def make_aware(unaware):
	aware = timezone.make_aware(unaware, timezone.get_current_timezone())
	return aware

class Command(BaseCommand):

	def handle(self, *args, **options):


		api_key = "61953c86d345eb2b23b2a53d50edbf5c"
		lat = 44.97257
		lon = -93.10827255249023
		try:
			forecast = forecastio.load_forecast(api_key, lat, lon)

			byHour = forecast.hourly()
			byDay = forecast.daily()
			currently = forecast.currently()
		
			try:
				wind_speed = currently.windSpeed
				wind_dir = currently.windBearing
				if 101.25 <= wind_dir <  123.75: 
					dir = "ESE"
				elif 11.25 <= wind_dir <  33.75: 
					dir = "NNE"
				elif 123.75 <= wind_dir <  146.25: 
					 dir = "SE"
				elif 146.25 <= wind_dir <  168.75: 
					dir = "SSE"
				elif 168.75 <= wind_dir <  191.25: 
					dir = "S"
				elif 191.25 <= wind_dir <  213.75: 
					dir = "SSW"
				elif 213.75 <= wind_dir <  236.25: 
					dir = "SW"
				elif 236.25 <= wind_dir <  258.75: 
					dir = "WSW"
				elif 258.75 <= wind_dir <  281.25: 
					dir = "W"
				elif 281.25 <= wind_dir <  303.75: 
					dir = "WNW"
				elif 303.75 <= wind_dir <  326.25: 
					dir = "NW"
				elif 326.25 <= wind_dir <  348.75: 
					dir = "NNW"
				elif 33.75 <= wind_dir <  56.25: 
					dir = "NE"
				elif 348.75 <= wind_dir <  360.25: 
					dir = "N"
				elif 0 <= wind_dir <  11.25: 
					dir = "N"
				elif 56.25 <= wind_dir <  78.75: 
					dir = "ENE"
				elif 78.75 <= wind_dir <  101.25: 
					dir = "E"
				else: dir = ""
			except:
				wind_mph = "N/A"
				dir = ""

		except:
			wx_dict = {'current_time': datetime.datetime(1900, 1, 1, 1, 1),
				   'current_icon': "Error01",
				   'temp': 999,
				   'skies': "Error01",
				   'wind': "Error01",
				   'current_forecast': "Error01",
				   'fcst1_time': datetime.datetime(1900, 1, 1, 1, 1),
				   'fcst1_icon': "Error01",
				   'fcst1': "Error01",
				   'fcst2_time': datetime.datetime(1900, 1, 1, 1, 1),
				   'fcst2_icon': "Error01",
				   'fcst2': "Error01",
				   'fcst3_time': datetime.datetime(1900, 1, 1, 1, 1),
				   'fcst3_icon': "Error01",
				   'fcst3': "Error01",
				   'fcst4_time': datetime.datetime(1900, 1, 1, 1, 1),
				   'fcst4_icon': "Error01",
				   'fcst4': "Error01",
				   'fcst5_time': datetime.datetime(1900, 1, 1, 1, 1),
				   'fcst5_icon': "Error01",
				   'fcst5': "Error01",
				   }


		wx_dict = {'current_time': make_aware(currently.time),
				   'current_icon': currently.icon,
				   'temp': int(currently.temperature),
				   'skies': currently.summary,
				   'wind': dir + " " + str(int(wind_speed)),
				   'current_forecast': byHour.summary + " High " + str(int(byDay.data[0].temperatureMax)) + ". " + byDay.summary,
				   'fcst1_time': make_aware(byDay.data[1].time),
				   'fcst1_icon': byDay.data[1].icon,
				   'fcst1': byDay.data[1].summary + " High " + str(int(byDay.data[1].temperatureMax)) + ".",
				   'fcst2_time': make_aware(byDay.data[2].time),
				   'fcst2_icon': byDay.data[2].icon,
				   'fcst2': byDay.data[2].summary + " High " + str(int(byDay.data[2].temperatureMax)) + ".",
				   'fcst3_time': make_aware(byDay.data[3].time),
				   'fcst3_icon': byDay.data[3].icon,
				   'fcst3': byDay.data[3].summary + " High " + str(int(byDay.data[3].temperatureMax)) + ".",
				   'fcst4_time': make_aware(byDay.data[4].time),
				   'fcst4_icon': byDay.data[4].icon,
				   'fcst4': byDay.data[4].summary + " High " + str(int(byDay.data[4].temperatureMax)) + ".",
				   'fcst5_time': make_aware(byDay.data[5].time),
				   'fcst5_icon': byDay.data[5].icon,
				   'fcst5': byDay.data[5].summary + " High " + str(int(byDay.data[5].temperatureMax)) + ".",
				   }
				   
		Weather.objects.filter(pk=1).update(**wx_dict)

