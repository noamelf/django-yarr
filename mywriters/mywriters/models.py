from django.db import models

class Catalogue(models.Model):
    writer = models.TextField()
    feed_url = models.URLField()

# class UserCatalogue(models.Model):
#     models.ForeignKey(Reporter, on_delete=models.CASCADE)