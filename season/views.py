from django.template import Context, loader
from season.models import Season, season_choice, player_choice
from gamemaker.views import context
from section.models import Page, Item
from photo.models import Photo
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

def season_params():
    seasons = Season.objects.all().order_by('year')
    count = len(seasons)
    first_season = seasons[0].year
    last_season = seasons[count - 1].year
    return (seasons, first_season, last_season, count)

#view for the History page
def prior(request):
    random_seasons = season_params()[0].order_by('?')
    count = season_params()[3]
    column_counts = count/4
    home_pk = Page.objects.get(header='Prior Seasons').pk
    content_list = Item.objects.filter(page = home_pk, published = True).order_by('position')
         
    t = loader.get_template('season/prior.html')
    c = Context({
        'seasons': season_params()[0],
        'count': season_params()[3],
        'column_counts': column_counts,
        'content_list': content_list,
        'wins': context()['wins'],
        'losses': context()['losses'],
        'ties': context()['ties'],
        'pastWins': context()['pastWins'],
        'pastLosses': context()['pastLosses'],
        'pastTies': context()['pastTies'],
        'random_seasons': random_seasons,
        'season_choice': season_choice,
        'player_choice': player_choice,	
    })
    return HttpResponse(t.render(c))

#Season detail pages:
def season_detail(request, season):
    current_year = timezone.now().year
    season_prior = Season.objects.get(year=season)
    roster = season_prior.roster
    photos = Photo.objects.filter(year=season)
    t = loader.get_template('season/season_detail.html')
    c = Context({
	    'current_year': current_year,
	    'season_prior': season_prior,
	    'roster': roster,
	    'photos': photos,
	    'seasons': season_params()[0],
	    'first_season': season_params()[1],
	    'last_season': season_params()[2],
    })
    return HttpResponse(t.render(c))


def season_quicklink(request):
    if request.method == "GET":
	    form = season_choice(request.GET)
	    if form.is_valid():
	        season = form.cleaned_data['choice'].year
	        redirect = '/season_detail/' + str(season)
	        
	    return HttpResponseRedirect(redirect)


def player_quicklink(request):
    if request.method == "GET":
	    form = player_choice(request.GET)
	    if form.is_valid():
	        player = form.cleaned_data['choice'].pk
	        redirect = '/player_detail/' + str(player)
	        
	    return HttpResponseRedirect(redirect)

def priorlinks(request):
    count = season_params()[3]
    column_counts = count/4
    t = loader.get_template('season/priorlinks.html')
    c = Context({
        'seasons': season_params()[0],
        'count': count,
        'column_counts': column_counts,
    })
    return HttpResponse(t.render(c))
 