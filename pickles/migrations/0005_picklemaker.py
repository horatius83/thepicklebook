# Generated by Django 4.0.3 on 2022-03-22 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pickles', '0004_auto_20220320_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='PickleMaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
            ],
        ),
    ]
