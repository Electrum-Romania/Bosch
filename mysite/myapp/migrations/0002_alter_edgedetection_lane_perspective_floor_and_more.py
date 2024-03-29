# Generated by Django 4.1.5 on 2023-02-21 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edgedetection',
            name='lane_perspective_floor',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='edgedetection',
            name='lane_perspective_roof',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='edgedetection',
            name='lane_perspective_startfloor',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='edgedetection',
            name='lane_perspective_startroof',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='edgedetection',
            name='lane_perspective_stopfloor',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='edgedetection',
            name='lane_perspective_stoproof',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
