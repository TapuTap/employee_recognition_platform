# Generated by Django 4.2.2 on 2023-07-12 06:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('goals_management', '0012_review_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created date'),
        ),
    ]