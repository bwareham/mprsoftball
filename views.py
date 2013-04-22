from django.template import Context, loader
from gamemaker.models import Game
from section.models import Page, Item
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
    period = latest_wx.findall(".//time-layout[@summarization='12hourly']/start-valid-time[@period-name]")
    period1 = period[0].get('period-name')
    period2 = period[1].get('period-name')
    period3 = period[2].get('period-name')
    fcst = latest_wx.findall(".//wordedForecast/*")
    fcst1 = fcst[1].text
    fcst2 = fcst[2].text
    fcst3 = fcst[3].text
    
	#Get game info
    played_games_list = Game.objects.filter(DateTime__lte=timezone.now()).order_by('DateTime')
    latest_games_list = Game.objects.filter(DateTime__gte=timezone.now()).order_by('DateTime')    
    home_pk = Page.objects.get(header='Home').pk
    content_list = Item.objects.filter(page = home_pk, published = True).order_by('position')
    t = loader.get_template('main.html')
    c = Context({
        'current_temp': current_temp,
        'sky': sky,
        'period1': period1,
        'period2': period2,
        'period3': period3,
        'fcst1': fcst1,
        'fcst2': fcst2,
        'fcst3': fcst3,
        'latest_games_list': latest_games_list,
        'played_games_list': played_games_list,
        'content_list': content_list,
    })
    return HttpResponse(t.render(c))


def directions(request):
    latest_games_list = Game.objects.filter(DateTime__gte=timezone.now()).order_by('DateTime')
    t = loader.get_template('directions.html')
    c = Context({
        'latest_games_list': latest_games_list,
    })
    return HttpResponse(t.render(c))

def index(request):
    return HttpResponse("This works")