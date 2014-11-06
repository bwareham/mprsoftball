from django.template import Context, loader
from gamemaker.models import Game, PlayedGames, LatestGames
from section.models import Page, Item
from photo.models import Photo
from django.http import HttpResponse
from django.template.response import TemplateResponse
import forecastio

def main(request):
    #Get latest wx info from forecast.io
	api_key = "61953c86d345eb2b23b2a53d50edbf5c"
	lat = 44.97257
	lon = -93.10827255249023
	try:
		forecast = forecastio.load_forecast(api_key, lat, lon)
		current_forecast = forecast.hourly().summary
		skies = forecast.currently().summary
		temp = forecast.currently().temperature

		try:
			wind_speed = forecast.currently().windSpeed
			wind_dir = forecast.currently().windBearing
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
		current_temp = "n/a"
        sky  = "n/a"
        #dir  = ""
        wind_mph  = " "
        period1  = "Forecast"
        period2  = " "
        period3  = " "
        fcst1  = "n/a"
        fcst2  = "n/a"
        fcst3 = "n/a"


    
	#Get game info  
	latest_games_list = LatestGames()
	played_games_list = PlayedGames()
	home_pk = Page.objects.get(header='Home').pk
	content_list = Item.objects.filter(page = home_pk, published = True).order_by('position')
	photos = Photo.objects.all()
	t = loader.get_template('main.html')
	c = Context({
		'current_temp': int(temp),
		'sky': skies,
		'dir': dir,
		'wind_mph': wind_speed,
		'period1': period1,
		'period2': period2,
		'period3': period3,
		'fcst1': fcst1,
		'fcst2': fcst2,
		'fcst3': fcst3,
		'latest_games_list': latest_games_list,
		'played_games_list': played_games_list,
		'content_list': content_list,
		'photos': photos,
	})
	return HttpResponse(t.render(c))


def directions(request):
	return TemplateResponse(request, 'directions.html', {})

