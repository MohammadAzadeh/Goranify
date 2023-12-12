from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Artist, Song, Album, Remix
from .forms import SongSearchForm

class HomeView(View):
    """View for the home page displaying a list of songs."""
    search_form = SongSearchForm

    def get(self, request):
        """
        Handles GET requests for the home page.

        Retrieves a list of songs based on search parameters or page number.

        Parameters:
        - request: The HTTP request object.

        Returns:
        - Rendered HTML with the list of songs.
        """
        songs = Song.objects.all()
        if songs.count() % 10 == 0:
            page_count = songs.count() // 10
        else:
            page_count = (songs.count() // 10) + 1
        page = 1

        if request.GET.get('search'):
            text_query = songs.filter(text__contains=request.GET['search'])
            name_query = songs.filter(name__contains=request.GET['search'])
            artist_query = songs.filter(artists__contains=request.GET['search'])
            songs = text_query | name_query | artist_query

        elif request.GET.get('page'):
            page = int(request.GET['page'])
        
        songs = songs[(page-1)*10:(page)*10]
        return render(request, 'home/home.html', {'songs': songs, 'search_form': self.search_form, 'page': page, 'page_count': page_count})

class SongView(View):
    """View for displaying details of a single song."""
    search_form = SongSearchForm

    def get(self, request, song_id):
        """
        Handles GET requests for displaying details of a single song.

        Parameters:
        - request: The HTTP request object.
        - song_id: The ID of the song to display.

        Returns:
        - Rendered HTML with the details of the specified song.
        """
        song = get_object_or_404(Song, pk=song_id)
        return render(request, 'home/song.html', {'song': song, 'search_form': self.search_form})


class SongCategoryView(View):
    """View for displaying a list of songs based on a category."""
    search_form = SongSearchForm

    def get(self, request, category_slug):
        """
        Handles GET requests for displaying a list of songs based on a category.

        Parameters:
        - request: The HTTP request object.
        - category_slug: The slug of the category to filter songs.

        Returns:
        - Rendered HTML with the list of songs belonging to the specified category.
        """
        songs = Song.objects.filter(category_id__slug=category_slug)
        if songs.count() % 10 == 0:
            page_count = songs.count() // 10
        else:
            page_count = (songs.count() // 10) + 1
        page = 1

        if request.GET.get('page'):
            page = int(request.GET['page'])
        songs = songs[(page-1)*10:(page)*10]
        return render(request, 'home/category.html', {'songs': songs, 'search_form': self.search_form, 'page': page, 'page_count': page_count})

class SongArtistView(View):
    """View for displaying a list of songs based on an artist."""
    search_form = SongSearchForm

    def get(self, request, artist_slug):
        """
        Handles GET requests for displaying a list of songs based on an artist.

        Parameters:
        - request: The HTTP request object.
        - artist_slug: The slug of the artist to filter songs.

        Returns:
        - Rendered HTML with the list of songs associated with the specified artist.
        """
        artist = get_object_or_404(Artist, slug=artist_slug)
        songs = Song.objects.filter(artists__contains=artist.name)
        if songs.count() % 10 == 0:
            page_count = songs.count() // 10
        else:
            page_count = (songs.count() // 10) + 1
        page = 1

        if request.GET.get('page'):
            page = int(request.GET['page'])
        songs = songs[(page-1)*10:(page)*10]
        return render(request, 'home/artist.html', {'songs': songs, 'search_form': self.search_form, 'page': page, 'page_count': page_count})

class SongAlbumsView(View):
    """View for displaying a list of albums."""
    search_form = SongSearchForm

    def get(self, request):
        """
        Handles GET requests for displaying a list of albums.

        Parameters:
        - request: The HTTP request object.

        Returns:
        - Rendered HTML with the list of albums.
        """
        albums = Album.objects.all()
        if albums.count() % 10 == 0:
            page_count = albums.count() // 10
        else:
            page_count = (albums.count() // 10) + 1
        page = 1

        if request.GET.get('page'):
            page = int(request.GET['page'])
        albums = Album.objects.all()[(page-1)*10:(page)*10]
        return render(request, 'home/albums.html', {'albums': albums, 'search_form': self.search_form, 'page': page, 'page_count': page_count})

class SongAlbumView(View):
    """View for displaying a list of songs based on an album."""
    search_form = SongSearchForm

    def get(self, request, album_id, album_slug):
        """
        Handles GET requests for displaying a list of songs based on an album.

        Parameters:
        - request: The HTTP request object.
        - album_id: The ID of the album to filter songs.
        - album_slug: The slug of the album to filter songs.

        Returns:
        - Rendered HTML with the list of songs belonging to the specified album.
        """
        songs = Song.objects.filter(album_id__id=album_id)
        songs = songs.filter(album_id__slug=album_slug)
        return render(request, 'home/album.html', {'songs': songs, 'search_form': self.search_form})

class SongRemixesView(View):
    """View for displaying a list of remixes."""
    search_form = SongSearchForm

    def get(self, request):
        """
        Handles GET requests for displaying a list of remixes.

        Parameters:
        - request: The HTTP request object.

        Returns:
        - Rendered HTML with the list of remixes.
        """
        remixes = Remix.objects.all()
        if remixes.count() % 10 == 0:
            page_count = remixes.count() // 10
        else:
            page_count = (remixes.count() // 10) + 1
        page = 1
        if request.GET.get('page'):
            page = int(request.GET['page'])
        remixes = Remix.objects.all()[(page-1)*10:(page)*10]
        return render(request, 'home/remixes.html', {'remixes': remixes, 'search_form': self.search_form, 'page': page, 'page_count': page_count})

class SongRemixView(View):
    """View for displaying details of a single remix."""
    search_form = SongSearchForm

    def get(self, request, remix_id):
        """
        Handles GET requests for displaying details of a single remix.

        Parameters:
        - request: The HTTP request object.
        - remix_id: The ID of the remix to display.

        Returns:
        - Rendered HTML with the details of the specified remix.
        """
        remix = get_object_or_404(Remix, id=remix_id)
        return render(request, 'home/remix.html', {'remix': remix, 'search_form': self.search_form})
