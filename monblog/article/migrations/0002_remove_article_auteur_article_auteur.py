# Generated by Django 5.1 on 2024-09-04 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='auteur',
        ),
        migrations.AddField(
            model_name='article',
            name='auteur',
            field=models.ManyToManyField(to='article.auteur'),
        ),
    ]
