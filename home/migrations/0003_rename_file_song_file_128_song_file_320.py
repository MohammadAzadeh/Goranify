# Generated by Django 4.1 on 2022-08-26 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_song_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='file',
            new_name='file_128',
        ),
        migrations.AddField(
            model_name='song',
            name='file_320',
            field=models.FileField(blank=True, null=True, upload_to='songs'),
        ),
    ]