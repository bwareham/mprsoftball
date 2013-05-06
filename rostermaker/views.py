from django.template import Context, loader
from rostermaker.models import Player, HOF
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
    player = Player.objects.get(pk=player_id)
    seasons = player.roster.all().order_by('year')
    hof = HOF.objects.filter(player=player_id).order_by('yearEntered')
    t = loader.get_template('rostermaker/player_detail.html')
    c = Context({
        'player': player,
        'seasons': seasons,
        'hof': hof,
    })
    return HttpResponse(t.render(c))
    