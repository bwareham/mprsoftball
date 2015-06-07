from django.template import Context, loader
from gamemaker.models import Game, PlayedGames, LatestGames
from section.models import Page, Item
from photo.models import Photo
from weathergrab.models import Weather
from django.http import HttpResponse
from django.template.response import TemplateResponse
import forecastio

def main(request):
    #Get wx info from forecast.io by way of grab.py management command
	weather = Weather.objects.get(pk=1)
	current_time = weather.current_time
	current_forecast = weather.current_forecast
	skies = weather.skies
	temp = weather.temp
	wind_mph = weather.wind
	current_forecast = weather.current_forecast
	fcst1_time = weather.fcst1_time
	fcst1_icon = weather.fcst1_icon
	fcst1 = weather.fcst1
	fcst2_time = weather.fcst2_time
	fcst2_icon = weather.fcst2_icon
	fcst2 = weather.fcst2
	fcst3_time = weather.fcst3_time
	fcst3_icon = weather.fcst3_icon
	fcst3 = weather.fcst3
	fcst4_time = weather.fcst4_time
	fcst4_icon = weather.fcst4_icon
	fcst4 = weather.fcst4
	fcst5_time = weather.fcst5_time
	fcst5_icon = weather.fcst5_icon
	fcst5 = weather.fcst5

    
	#Get game info  
	latest_games_list = LatestGames()
	played_games_list = PlayedGames()
	home_pk = Page.objects.get(header='Home').pk
	content_list = Item.objects.filter(page = home_pk, published = True).order_by('position')
	photos = Photo.objects.all()
	t = loader.get_template('main.html')
	c = Context({
		'current_time': current_time,
		'current_temp': int(temp),
		'sky': skies,
		'wind_mph': wind_mph,
		'current_forecast': current_forecast,
		'fcst1': fcst1,
		'fcst2': fcst2,
		'fcst3': fcst3,
		'fcst4': fcst4,
		'fcst5': fcst5,
		'fcst1_time': fcst1_time,
		'fcst2_time': fcst2_time,
		'fcst3_time': fcst3_time,
		'fcst4_time': fcst4_time,
		'fcst5_time': fcst5_time,
		'latest_games_list': latest_games_list,
		'played_games_list': played_games_list,
		'content_list': content_list,
		'photos': photos,
	})
	return HttpResponse(t.render(c))


def directions(request):
	return TemplateResponse(request, 'directions.html', {})

