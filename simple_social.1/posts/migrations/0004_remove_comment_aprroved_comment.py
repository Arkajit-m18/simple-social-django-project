# Generated by Django 2.1.7 on 2019-04-03 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20190403_0321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='aprroved_comment',
        ),
    ]