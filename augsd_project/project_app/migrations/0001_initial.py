# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-02 05:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SubSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.CharField(max_length=7)),
                ('startTime', models.IntegerField()),
                ('endTime', models.IntegerField()),
                ('courseCode', models.CharField(max_length=10)),
                ('instructor1', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='instructor1', to='project_app.Instructor')),
                ('instructor2', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='instructor2', to='project_app.Instructor')),
            ],
        ),
    ]
