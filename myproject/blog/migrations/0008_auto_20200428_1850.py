# Generated by Django 3.0.5 on 2020-04-28 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_article_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='catagory',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='descreaption',
            new_name='description',
        ),
    ]