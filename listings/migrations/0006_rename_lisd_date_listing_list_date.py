# Generated by Django 3.2.4 on 2021-07-03 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_auto_20210703_0725'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='lisd_date',
            new_name='list_date',
        ),
    ]
