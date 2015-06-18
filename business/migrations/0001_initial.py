# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorful.fields


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
                ('medal', models.ImageField(null=True, upload_to=b'business', blank=True)),
            ],
            options={
                'verbose_name': 'Category Employee',
                'verbose_name_plural': 'Category Employees',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CustomCategoryService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=750, null=True, blank=True)),
                ('color', colorful.fields.RGBColorField()),
            ],
            options={
                'verbose_name': 'Custom Category Service',
                'verbose_name_plural': 'Custom Category Services',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DefaultCategoryService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=750, null=True, blank=True)),
                ('color', colorful.fields.RGBColorField()),
            ],
            options={
                'verbose_name': 'Default Category Service',
                'verbose_name_plural': 'Default Category Services',
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
                'verbose_name_plural': 'Employees',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('work_day', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Holiday',
                'verbose_name_plural': 'Holidays',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('event_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='schedule.Event')),
                ('reference', models.CharField(max_length=750, null=True, blank=True)),
                ('urgency_status', models.CharField(default=b'NO', max_length=2, choices=[(b'NO', b'Normal'), (b'HI', b'High'), (b'CT', b'Critical')])),
                ('custom_category_service', models.OneToOneField(related_name=b'service', to='business.CustomCategoryService')),
                ('default_category_service', models.ForeignKey(related_name=b'services', to='business.DefaultCategoryService')),
                ('employees', models.ManyToManyField(related_name=b'services', to='business.Employee')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
            bases=('schedule.event',),
        ),
    ]
