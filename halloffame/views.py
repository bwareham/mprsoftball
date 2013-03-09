from django.template import Context, loader
from gamemaker.models import Game
from section.models import Page, Item
from django.http import HttpResponse
from django.utils import timezone

def hall_main(request):
    latest_games_list = Game.objects.filter(DateTime__gte=timezone.now()).order_by('DateTime')
    home_pk = Page.objects.get(header='Hall of Fame').pk
    content_list = Item.objects.filter(page = home_pk, published = True).order_by('position')
    t = loader.get_template('halloffame/hall_main.html')
    c = Context({
        'latest_games_list': latest_games_list,
        'content_list': content_list,
    })
    return HttpResponse(t.render(c))