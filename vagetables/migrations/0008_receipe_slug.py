# Generated by Django 5.0.4 on 2024-07-06 07:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vagetables', '0007_alter_reportcard_date_of_report_card_generation'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipe',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2024, 7, 6, 7, 24, 37, 729628, tzinfo=datetime.timezone.utc), unique=True),
            preserve_default=False,
        ),
    ]
