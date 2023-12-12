from .models import Artist, Song

all_artists = Artist.objects.all()
artists_count = all_artists.count()
def artists1(request):
    return {'artists1': Artist.objects.all()[:int(artists_count/2)]}

def artists2(request):
    return {'artists2': Artist.objects.all()[int(artists_count/2):]}

def all_songs(request):
    return {'all_songs': Song.objects.all()}