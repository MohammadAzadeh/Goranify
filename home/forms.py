from django import forms


class SongSearchForm(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control me-2", 'type': "search", 'placeholder':"جستجوی اسم آهنگ یا خواننده ...", 'aria-label': "Search"}))
