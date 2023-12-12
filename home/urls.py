from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('song/<int:song_id>', views.SongView.as_view(), name='song'),
    path('category/<slug:category_slug>/', views.SongCategoryView.as_view(), name='song_category'),
    path('artist/<slug:artist_slug>/', views.SongArtistView.as_view(), name='song_artist'),
    path('albums/', views.SongAlbumsView.as_view(), name='song_albums'),
    path('album/<int:album_id>/<slug:album_slug>/', views.SongAlbumView.as_view(), name='song_album'),
    path('remixes/', views.SongRemixesView.as_view(), name='song_remixes'),
    path('remix/<int:remix_id>/', views.SongRemixView.as_view(), name='song_remix'),
]