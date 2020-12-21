# Generated by Django 3.1.4 on 2020-12-21 21:02

import os

from django.db import migrations
from django.db.backends.postgresql.schema import DatabaseSchemaEditor
from django.db.migrations.state import StateApps


def createsuperuser(apps: StateApps, schema_editor: DatabaseSchemaEditor) -> None:
    """
    Dynamically create an admin user as part of a migration
    Password is pulled from Secret Manger (previously created as part of tutorial)
    """
    admin_password = os.getenv("SUPERUSER_PASSWORD")

    # Create a new user using acquired password
    from django.contrib.auth.models import User

    User.objects.create_superuser("admin", password=admin_password)


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [migrations.RunPython(createsuperuser)]