# Generated by Django 3.2.6 on 2021-08-31 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0003_auto_20210830_2003'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-post_date']},
        ),
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
