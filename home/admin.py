from django.contrib import admin
from .models import Artist, Song, Category, Album, Remix

admin.site.register(Artist)
admin.site.register(Category)
admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Remix)