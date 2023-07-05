# Generated by Django 4.2.2 on 2023-07-05 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals_management', '0008_alter_review_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='goals_review',
            field=models.PositiveSmallIntegerField(choices=[(0, '🔴 Nearly Meets Expectations'), (8, '🟡 Meets Expectations'), (15, '🟢 Exceeds Expectations')], db_index=True, default=0, verbose_name='goals review'),
        ),
        migrations.AlterField(
            model_name='review',
            name='innovation_review',
            field=models.PositiveSmallIntegerField(choices=[(0, '🔴 Nearly Meets Expectations'), (8, '🟡 Meets Expectations'), (15, '🟢 Exceeds Expectations')], db_index=True, default=0, verbose_name='innovation review'),
        ),
        migrations.AlterField(
            model_name='review',
            name='teamwork_review',
            field=models.PositiveSmallIntegerField(choices=[(0, '🔴 Nearly Meets Expectations'), (8, '🟡 Meets Expectations'), (15, '🟢 Exceeds Expectations')], db_index=True, default=0, verbose_name='teamwork review'),
        ),
        migrations.AlterField(
            model_name='review',
            name='total_review',
            field=models.PositiveSmallIntegerField(choices=[(0, '🔴 Nearly Meets Expectations'), (8, '🟡 Meets Expectations'), (15, '🟢 Exceeds Expectations')], db_index=True, default=0, verbose_name='total review'),
        ),
        migrations.AlterField(
            model_name='review',
            name='work_ethics_review',
            field=models.PositiveSmallIntegerField(choices=[(0, '🔴 Nearly Meets Expectations'), (8, '🟡 Meets Expectations'), (15, '🟢 Exceeds Expectations')], db_index=True, default=0, verbose_name='work ethics review'),
        ),
    ]
