# Generated by Django 3.2.4 on 2021-07-03 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20210701_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_1',
            field=models.ImageField(blank=True, upload_to='media/photos/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_2',
            field=models.ImageField(blank=True, upload_to='media/photos/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_3',
            field=models.ImageField(blank=True, upload_to='media/photos/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_4',
            field=models.ImageField(blank=True, upload_to='media/photos/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_5',
            field=models.ImageField(blank=True, upload_to='media/photos/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_6',
            field=models.ImageField(blank=True, upload_to='media/photos/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_main',
            field=models.ImageField(upload_to='media/photos/%y/%m/%d'),
        ),
    ]
