# Generated by Django 3.2.12 on 2022-03-02 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_auto_20220302_1551'),
        ('users', '0002_auto_20220302_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favs',
            field=models.ManyToManyField(null=True, related_name='favs', to='rooms.Room'),
        ),
    ]
