# Generated by Django 2.1.7 on 2019-04-01 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190401_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='restaurant',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='menus',
            field=models.ManyToManyField(to='api.Menu'),
        ),
    ]
