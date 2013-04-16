from django.template import Context, loader
from rostermaker.models import Player
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