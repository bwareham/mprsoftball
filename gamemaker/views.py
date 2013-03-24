from django.template import Context, loader
from gamemaker.models import Game, Stat
from section.models import Page, Item
from django.http import HttpResponse
from django.utils import timezone
from rostermaker.models import Player
from django.db.models import Sum

def current(request):
    latest_games_list = Game.objects.filter(DateTime__gte=timezone.now()).order_by('DateTime')
    played_games_list = Game.objects.filter(DateTime__lte=timezone.now()).order_by('-DateTime')
    home_pk = Page.objects.get(header='This Season').pk
    content_list = Item.objects.filter(page = home_pk, published = True).order_by('position')
    t = loader.get_template('gamemaker/current.html')
    c = Context({
        'latest_games_list': latest_games_list,
        'played_games_list': played_games_list,
        'content_list': content_list,
    })
    return HttpResponse(t.render(c))


def stats(request):
    #get this year's stats, create sums for each player and make dictionary
    current_stats = Stat.objects.filter(game__DateTime__year=timezone.now().year)
    stats_dict = current_stats.values('player')
    totals = stats_dict.annotate(
        ab=Sum('AB'),
		sing=Sum('single'),
		doub=Sum('double'),
		trip=Sum('triple'),
		hr=Sum('HR'),
		sac=Sum('SAC'),
		bb=Sum('BB'),
		so=Sum('SO'),
		runs=Sum('R'),
		rbi=Sum('RBI'),
		)
		
	#add batting average and player name to dictionary
    for item in totals:
	    if item['sing']:
	        a = item['sing']
	    else:
	        a=0
	    if item['doub']:
	        b=item['doub']
	    else:
	        b=0
	    if item['trip']:
	        c=item['trip']
	    else:
	        c=0
	    if item['hr']:
	        d=item['hr']
	    else:
	        d=0
	    hits = a + b + c + d
	    avg = hits/float(item['ab'])
	    item['avg']=avg
	    key = item['player']
	    name = Player.objects.get(pk=key)
	    item['name']=name
    t = loader.get_template('gamemaker/stats.html')
    c = Context({
        'totals': totals,
    })
    return HttpResponse(t.render(c))
