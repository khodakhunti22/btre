# Generated by Django 3.2.4 on 2021-07-03 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='photo',
            field=models.ImageField(upload_to='media/photos/%Y/%m/%d'),
        ),
    ]
