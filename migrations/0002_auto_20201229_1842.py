# Generated by Django 3.1.4 on 2020-12-29 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywriters', '0004_auto_20201229_1842'),
        ('yarr', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='user',
        ),
        migrations.AddField(
            model_name='feed',
            name='users',
            field=models.ManyToManyField(to='mywriters.UserFeeds'),
        ),
    ]
