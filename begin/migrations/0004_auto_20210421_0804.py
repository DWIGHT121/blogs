# Generated by Django 3.2 on 2021-04-21 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('begin', '0003_auto_20210420_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ImageField(default='media/noimg2.png', upload_to=''),
        ),
        migrations.CreateModel(
            name='ArticlesImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='')),
                ('article', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='begin.articles')),
            ],
        ),
    ]
