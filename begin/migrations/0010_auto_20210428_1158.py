# Generated by Django 3.2 on 2021-04-28 11:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('begin', '0009_alter_articles_start_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articles',
            old_name='field',
            new_name='field1',
        ),
        migrations.AddField(
            model_name='articles',
            name='field2',
            field=models.TextField(default=django.utils.timezone.now, max_length=50000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articles',
            name='topic',
            field=models.CharField(max_length=200),
        ),
    ]
