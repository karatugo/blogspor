# Generated by Django 2.2 on 2020-01-24 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200124_1108'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['publish_date', 'updated', 'timestamp']},
        ),
    ]
