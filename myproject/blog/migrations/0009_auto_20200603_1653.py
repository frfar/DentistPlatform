# Generated by Django 3.0.5 on 2020-06-03 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200428_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(upload_to='images', verbose_name='تصویر مقاله'),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='blog.Category', verbose_name='ﻪﺘﺳﺩ ﺭیﺯ'),
        ),
        migrations.AlterField(
            model_name='category',
            name='position',
            field=models.IntegerField(verbose_name='پوزیشن'),
        ),
    ]
