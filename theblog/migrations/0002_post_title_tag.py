# Generated by Django 3.2.6 on 2021-08-30 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Riskool Express', max_length=255),
        ),
    ]
