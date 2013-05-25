from django.http import HttpResponse
from django.template import Context, loader
from section.models import Page, Item
from photo.models import Photo
from django.http import HttpResponse
from django.utils import timezone

def gallery_main(request):
    home_pk = Page.objects.get(header='Photo Gallery').pk
    content_list = Item.objects.filter(page = home_pk, published = True).order_by('position')
    photos = Photo.objects.all().order_by('?')
    latest_pics = Photo.objects.all().order_by('-pk')
    t = loader.get_template('photo/gallery_main.html')
    c = Context({
        'content_list': content_list,
        'photos': photos,
        'latest_pics': latest_pics,
    })
    return HttpResponse(t.render(c))
    
def random_pics(request):
    photos = Photo.objects.all().order_by('?')
    t = loader.get_template('photo/random_pics.html')
    c = Context({
        'photos': photos,
    })
    return HttpResponse(t.render(c))
        
