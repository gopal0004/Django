# Generated by Django 5.0.4 on 2024-07-06 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagetables', '0008_receipe_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipe',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
