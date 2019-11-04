# Generated by Django 2.2.3 on 2019-11-04 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('title_en', models.CharField(max_length=40)),
                ('audience', models.IntegerField()),
                ('open_date', models.DateField()),
                ('genre', models.CharField(max_length=20)),
                ('watch_grade', models.CharField(max_length=20)),
                ('score', models.FloatField()),
                ('poster_url', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]
