# Generated by Django 3.2 on 2021-04-23 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('begin', '0005_articles_start_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='start_text',
            field=models.TextField(default=' ', max_length=100),
        ),
    ]
