from logging import getLogger

from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from mywriters.generate_feeds import haaretz
from yarr.models import Feed

logger = getLogger(__name__)


class Command(BaseCommand):
    help = "Generate RSS feed"

    def handle(self, *args, **options):
        for name, image, link, rss in haaretz.create_haaretz_feeds():
            self.stdout.write(f"Fetching {name}")
            try:
                Feed.objects.update_or_create(
                    title=name, site_url=link, defaults={"rss": rss, "image": image}
                )
            except IntegrityError as e:
                self.stdout.write(e)

        self.stdout.write(self.style.SUCCESS("Successfully generated feeds"))
