# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryEmployee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=750, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Category Employee',
                'verbose_name_plural': 'Category Employees ',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CategoryService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=750, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Category Service',
                'verbose_name_plural': 'Category Services ',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=750, null=True, blank=True)),
                ('category_employee', models.ForeignKey(related_name=b'employees', to='business.CategoryEmployee')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees ',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('event_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='schedule.Event')),
                ('reference', models.CharField(max_length=750, null=True, blank=True)),
                ('category_service', models.ForeignKey(related_name=b'services', to='business.CategoryService')),
                ('employees', models.ManyToManyField(related_name=b'services', to='business.Employee')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
            bases=('schedule.event',),
        ),
    ]
