# Generated by Django 4.0.3 on 2022-03-22 10:10

from django.db import migrations

def add_pickle_makers(apps, schema_editor):
    """Go through all of the pickles, and add maker column to its own table"""
    Pickle = apps.get_model('pickles', 'Pickle')
    PickleMaker = apps.get_model('pickles', 'PickleMaker')
    all_makers = set(x.maker for x in Pickle.objects.all())
    for maker in all_makers:
        pm = PickleMaker(name=maker)
        pm.save()

class Migration(migrations.Migration):

    dependencies = [
        ('pickles', '0005_picklemaker'),
    ]

    operations = [
        migrations.RunPython(add_pickle_makers)
    ]
