# Generated by Django 5.1.2 on 2024-11-18 16:27

import django.utils.timezone
import home.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_category_created_at_category_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=home.models.TimestampField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=home.models.TimestampField(auto_now=True),
        ),
    ]
