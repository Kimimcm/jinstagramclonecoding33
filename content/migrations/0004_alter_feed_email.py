# Generated by Django 3.2.12 on 2022-03-26 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_alter_feed_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
