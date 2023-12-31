# Generated by Django 4.2.2 on 2023-06-30 07:09

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('goals_management', '0003_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='goals_achievment',
            field=tinymce.models.HTMLField(blank=True, db_index=True, max_length=2000, null=True, verbose_name='goals achievment'),
        ),
        migrations.AlterField(
            model_name='review',
            name='total_review',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Nearly Meets Expectations'), (8, 'Meets Expectations'), (15, 'Exceeds Expectations')], db_index=True, default=0, verbose_name='total review'),
        ),
        migrations.AlterField(
            model_name='review',
            name='work_ethics',
            field=tinymce.models.HTMLField(blank=True, db_index=True, max_length=2000, null=True, verbose_name='work ethics'),
        ),
    ]
