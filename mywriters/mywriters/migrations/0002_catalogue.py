# Generated by Django 3.1.4 on 2020-12-26 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mywriters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.TextField()),
                ('feed_url', models.URLField()),
            ],
        ),
    ]