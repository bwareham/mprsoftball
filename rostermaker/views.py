from django.template import Context, loader
from rostermaker.models import Player, HOF
from photo.models import Photo
from section.models import Page, Item
from season.models import Season
from django.http import HttpResponse


def players(request):
    players_list = Player.objects.all().order_by('lastName', 'firstName')
    count = len(players_list)
    column_counts = count/4
    t = loader.get_template('rostermaker/players.html')
    c = Context({
        'players_list': players_list,
        'count': count,
        'column_counts': column_counts,
    })
    return HttpResponse(t.render(c))
    
def player_detail(request, player_id):
    s = Season.objects.all()
    player = Player.objects.get(pk=player_id)
    seasons = player.roster.all().order_by('year')
    hof = HOF.objects.filter(player=player_id).order_by('yearEntered')
    captain = s.filter(captains=player_id).order_by('year')
    rookie = s.filter(rookies=player_id).order_by('year')
    mvp = s.filter(mvp=player_id).order_by('year')
    battingchamp = s.filter(battingchamps=player_id).order_by('year')
    goldenglove = s.filter(goldengloves=player_id).order_by('year')
    mostimproved = s.filter(mostimproved=player_id).order_by('year')
    whippet = s.filter(whippet=player_id).order_by('year')
    bombat = s.filter(bombat=player_id).order_by('year')
    photos = Photo.objects.filter(player_tag=player)
    t = loader.get_template('rostermaker/player_detail.html')
    c = Context({
        'player': player,
        'seasons': seasons,
        'hof': hof,
        'captain': captain,
        'rookie': rookie,
        'mvp': mvp,
        'battingchamp': battingchamp,
        'goldenglove': goldenglove,
        'mostimproved': mostimproved,
        'whippet': whippet,
        'bombat': bombat,
        'photos': photos,
    })
    return HttpResponse(t.render(c))
    
def hall_main(request):
    h = HOF.objects.filter
    pipp = h(wing='WP').order_by('yearEntered','player')
    paige = h(wing='SP').order_by('yearEntered','player')
    main = h(wing='MN').order_by('yearEntered','player')
    ted = h(wing='TW').order_by('yearEntered','player')
    home_pk = Page.objects.get(header='Hall of Fame').pk
    content_list = Item.objects.filter(page = home_pk, published = True).order_by('position')
    t = loader.get_template('rostermaker/hall_main.html')
    c = Context({
        'pipp': pipp,
        'paige': paige,
        'main': main,
        'ted': ted,
        'content_list': content_list,
    })
    return HttpResponse(t.render(c))