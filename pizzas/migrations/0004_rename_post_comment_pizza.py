# Generated by Django 3.2 on 2021-12-12 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='pizza',
        ),
    ]
