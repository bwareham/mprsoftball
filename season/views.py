from django.template import Context, loader
from season.models import Season
from section.models import Page, Item
from django.http import HttpResponse
from django.utils import timezone

def prior(request):
    #latest_games_list = Game.objects.filter(DateTime__gte=timezone.now()).order_by('DateTime')
    seasons = Season.objects.all().order_by('year')
    count = len(seasons)
    column_counts = count/4
    home_pk = Page.objects.get(header='Prior Seasons').pk
    content_list = Item.objects.filter(page = home_pk, published = True).order_by('position')
    t = loader.get_template('season/prior.html')
    c = Context({
        'seasons': seasons,
        'count': count,
        'column_counts': column_counts,
        'content_list': content_list,
    })
    return HttpResponse(t.render(c))

#Season detail pages:
def season_detail(request, season):
    current_year = timezone.now().year
    season = Season.objects.get(year=season)
    roster = season.roster
    t = loader.get_template('season/season_detail.html')
    c = Context({
        'current_year': current_year,
		'season': season,
        'roster': roster,
    })
    return HttpResponse(t.render(c))
