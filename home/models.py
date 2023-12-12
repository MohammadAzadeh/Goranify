from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    cover = models.ImageField(upload_to='images/albums', blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Song(models.Model):
    main_artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True)
    artists = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    file_128 = models.FileField(upload_to='songs', blank=True, null=True)
    file_320 = models.FileField(upload_to='songs', blank=True, null=True)
    cover = models.ImageField(upload_to='images', blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    published = models.DateTimeField(auto_now_add=True)
    suggested = models.BooleanField(default=False)

    class Meta:
        ordering = ['-published']

    def text_lines(self):
        return str(self.text).split('\n')
    
    def __str__(self):
        return f'{self.name} - {self.artists}'

class Remix(models.Model):
    by = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    artists = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    file_128 = models.FileField(upload_to='songs', blank=True, null=True)
    file_320 = models.FileField(upload_to='songs', blank=True, null=True)
    cover = models.ImageField(upload_to='images/remixes', blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    published = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['-published']

    def text_lines(self):
        return str(self.text).split('\n')
    
    def __str__(self):
        return f'{self.name}'