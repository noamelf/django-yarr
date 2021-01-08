from django.core.management.base import BaseCommand
from mywriters.generate_feeds import haaretz
from yarr.models import Feed


class Command(BaseCommand):
    help = 'Generate RSS feed'

    def handle(self, *args, **options):
        for name, link, rss in haaretz.create_haaretz_feeds():
            obj, created = Feed.objects.update_or_create(
                title=name, site_url=link, defaults={'rss': rss}
            )
            print(obj)


        self.stdout.write(self.style.SUCCESS('Successfully generated feeds'))
