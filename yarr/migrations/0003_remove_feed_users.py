# Generated by Django 3.1.4 on 2020-12-29 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yarr', '0002_auto_20201229_1842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='users',
        ),
    ]
