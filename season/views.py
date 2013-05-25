from django.template import Context, loader
from season.models import Season
from gamemaker.models import Game
from section.models import Page, Item
from photo.models import Photo
from django.http import HttpResponse
from django.utils import timezone
from django.db.models import Sum, F

def prior(request):
    #latest_games_list = Game.objects.filter(DateTime__gte=timezone.now()).order_by('DateTime')
    seasons = Season.objects.all().order_by('year')
    count = len(seasons)
    column_counts = count/4
    home_pk = Page.objects.get(header='Prior Seasons').pk
    content_list = Item.objects.filter(page = home_pk, published = True).order_by('position')
    played_games_list = Game.objects.filter(DateTime__lte=timezone.now()).order_by('-DateTime')
    wins = played_games_list.filter(scoreMPR__gt=F('scoreOPP')).count()
    losses = played_games_list.filter(scoreOPP__gt=F('scoreMPR')).count()
    ties = wins = played_games_list.filter(scoreMPR__exact=F('scoreOPP')).count()
    pastWins = Season.objects.aggregate(Sum('wins'))
    pastLosses = Season.objects.aggregate(Sum('losses'))
    pastTies = Season.objects.aggregate(Sum('ties'))
    t = loader.get_template('season/prior.html')
    c = Context({
        'seasons': seasons,
        'count': count,
        'column_counts': column_counts,
        'content_list': content_list,
        'wins': wins,
        'losses': losses,
        'ties': ties,
        'pastWins': pastWins,
        'pastLosses': pastLosses,
        'pastTies': pastTies,
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
    })
    return HttpResponse(t.render(c))

