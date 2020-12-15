# Generated by Django 3.1.4 on 2020-12-14 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamer', '0002_auto_20201214_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='teamplay',
            field=models.CharField(default=0, max_length=8, verbose_name='TeamPlay'),
        ),
        migrations.AddField(
            model_name='user',
            name='teamplayfn',
            field=models.CharField(default=0, max_length=8, verbose_name='TeamPlay_Fortnite'),
        ),
        migrations.AddField(
            model_name='user',
            name='teamplayow',
            field=models.CharField(default=0, max_length=8, verbose_name='TeamPlay_Overwatch'),
        ),
    ]