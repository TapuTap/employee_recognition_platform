# Generated by Django 4.2.2 on 2023-06-28 08:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=150, null=True, verbose_name='title')),
                ('description', tinymce.models.HTMLField(blank=True, db_index=True, max_length=2000, null=True, verbose_name='description')),
                ('start_date', models.DateField(default=django.utils.timezone.now, verbose_name='start date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='end date')),
                ('priority', models.PositiveSmallIntegerField(choices=[(0, 'High'), (1, 'Medium'), (2, 'Low')], db_index=True, default=0, verbose_name='priority')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Planned'), (1, 'In progress'), (2, 'Complete'), (3, 'On hold'), (4, 'Cancelled')], db_index=True, default=0, verbose_name='status')),
                ('progress', models.PositiveSmallIntegerField(choices=[(0, '0 %'), (1, '10 %'), (2, '20 %'), (3, '30 %'), (4, '40 %'), (5, '50 %'), (6, '60 %'), (7, '70 %'), (8, '80 %'), (9, '90 %'), (10, '100 %')], db_index=True, default=0, verbose_name='progress')),
            ],
            options={
                'verbose_name': 'goal',
                'verbose_name_plural': 'goals',
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='first name')),
                ('last_name', models.CharField(max_length=50, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('hire_date', models.DateField(default=django.utils.timezone.now, verbose_name='hire date')),
                ('term_date', models.DateField(blank=True, null=True, verbose_name='termination date')),
                ('department', models.CharField(max_length=50, verbose_name='department')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Active'), (1, 'Terminated')], db_index=True, default=0, verbose_name='status')),
            ],
            options={
                'verbose_name': 'manager',
                'verbose_name_plural': 'managers',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='first name')),
                ('last_name', models.CharField(max_length=50, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('hire_date', models.DateField(default=django.utils.timezone.now, verbose_name='hire date')),
                ('term_date', models.DateField(blank=True, null=True, verbose_name='termination date')),
                ('position', models.CharField(max_length=50, verbose_name='position')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Active'), (1, 'Terminated')], db_index=True, default=0, verbose_name='status')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='goals_management.manager', verbose_name='manager')),
            ],
            options={
                'verbose_name': 'employee',
                'verbose_name_plural': 'employees',
            },
        ),
    ]
