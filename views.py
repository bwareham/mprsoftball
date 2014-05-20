from django.template import Context, loader
from gamemaker.models import Game, PlayedGames, LatestGames
from section.models import Page, Item
from photo.models import Photo
from django.http import HttpResponse
from django.utils import timezone
import urllib2
import xml.etree.ElementTree as ET

def main(request):
    #Get latest wx info from NWS
    response = urllib2.urlopen('http://forecast.weather.gov/MapClick.php?lat=44.97257&lon=-93.10827255249023&unit=0&lg=english&FcstType=dwml')
    xml = response.read()
    latest_wx = ET.fromstring(xml)
    temps = latest_wx.findall(".//temperature[@type='apparent']/value")
    current_temp = temps[0].text
    conditions = latest_wx.findall(".//data[@type='current observations']/parameters/weather/weather-conditions")[0].attrib
    sky = conditions.get('weather-summary')
    try:
        wind_speed = latest_wx.findall(".//wind-speed[@type='sustained']/value")[0].text
        wind_mph = int(float(wind_speed) * 1.15077945)
        dir_deg = int(latest_wx.findall(".//direction[@type='wind']/value")[0].text)
        if 101.25 <= dir_deg <  123.75: 
            dir = "ESE"
        elif 11.25 <= dir_deg <  33.75: 
            dir = "NNE"
        elif 123.75 <= dir_deg <  146.25: 
             dir = "SE"
        elif 146.25 <= dir_deg <  168.75: 
            dir = "SSE"
        elif 168.75 <= dir_deg <  191.25: 
            dir = "S"
        elif 191.25 <= dir_deg <  213.75: 
            dir = "SSW"
        elif 213.75 <= dir_deg <  236.25: 
            dir = "SW"
        elif 236.25 <= dir_deg <  258.75: 
            dir = "WSW"
        elif 258.75 <= dir_deg <  281.25: 
            dir = "W"
        elif 281.25 <= dir_deg <  303.75: 
            dir = "WNW"
        elif 303.75 <= dir_deg <  326.25: 
            dir = "NW"
        elif 326.25 <= dir_deg <  348.75: 
            dir = "NNW"
        elif 33.75 <= dir_deg <  56.25: 
            dir = "NE"
        elif 348.75 <= dir_deg <  360.25: 
            dir = "N"
        elif 0 <= dir_deg <  11.25: 
            dir = "N"
        elif 56.25 <= dir_deg <  78.75: 
            dir = "ENE"
        elif 78.75 <= dir_deg <  101.25: 
            dir = "E"
        else: dir = ""
    except:
        wind_mph = "N/A"
        dir = ""
    period = latest_wx.findall(".//time-layout[@summarization='12hourly']/start-valid-time[@period-name]")
    period1 = period[0].get('period-name')
    period2 = period[1].get('period-name')
    period3 = period[2].get('period-name')
    fcst = latest_wx.findall(".//wordedForecast/*")
    fcst1 = fcst[1].text
    fcst2 = fcst[2].text
    fcst3 = fcst[3].text
    
	#Get game info
    #played_games_list = Game.objects.filter(when__lte=timezone.now()).order_by('-when')
    #latest_games_list = Game.objects.filter(when__gte=timezone.now()).order_by('when')    
    latest_games_list = LatestGames()
    played_games_list = PlayedGames()
    home_pk = Page.objects.get(header='Home').pk
    content_list = Item.objects.filter(page = home_pk, published = True).order_by('position')
    photos = Photo.objects.all()
    t = loader.get_template('main.html')
    c = Context({
        'current_temp': current_temp,
        'sky': sky,
        'dir': dir,
        'wind_mph': wind_mph,
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
    latest_games_list = Game.objects.filter(when__gte=timezone.now()).order_by('when')
    t = loader.get_template('directions.html')
    c = Context({
        'latest_games_list': latest_games_list,
    })
    return HttpResponse(t.render(c))

def index(request):
    return HttpResponse("This works")