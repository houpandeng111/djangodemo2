# Generated by Django 3.0.7 on 2020-07-05 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_author_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]
