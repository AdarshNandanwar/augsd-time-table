# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-07 19:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseCode', models.CharField(max_length=10)),
                ('courseName', models.CharField(max_length=50)),
                ('midsemDateTime', models.DateTimeField()),
                ('compreDateTime', models.DateTimeField()),
                ('courseIC', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='InstructorIncharge', to='project_app.Instructor')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ltp', models.CharField(default='000', max_length=3)),
                ('course', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='section', to='project_app.Course')),
            ],
        ),
        migrations.RemoveField(
            model_name='subsection',
            name='courseCode',
        ),
        migrations.AddField(
            model_name='subsection',
            name='type',
            field=models.CharField(default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subsection',
            name='instructor1',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='subSection1', to='project_app.Instructor'),
        ),
        migrations.AlterField(
            model_name='subsection',
            name='instructor2',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='subSection2', to='project_app.Instructor'),
        ),
        migrations.AddField(
            model_name='subsection',
            name='section',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='subSection', to='project_app.Section'),
        ),
    ]