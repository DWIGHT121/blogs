# Generated by Django 3.2 on 2021-04-23 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('begin', '0007_alter_articles_start_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='start_text',
            field=models.TextField(max_length=100, null=True),
        ),
    ]