# Generated by Django 2.2 on 2020-10-21 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0005_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='subject',
            new_name='topic',
        ),
    ]
