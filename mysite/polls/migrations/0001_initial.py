# Generated by Django 5.0.8 on 2024-08-07 13:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('founded_date', models.DateField()),
                ('headquarters', models.CharField(max_length=100)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('founded_date', models.IntegerField(default=2000)),
                ('headquarters', models.CharField(max_length=200)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('release_year', models.PositiveIntegerField()),
                ('sales', models.DecimalField(decimal_places=2, max_digits=10)),
                ('genre', models.CharField(max_length=100)),
                ('platforms', models.CharField(max_length=200)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('description', models.TextField()),
                ('awards', models.TextField()),
                ('box_art_url', models.URLField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.company')),
                ('developers', models.ManyToManyField(to='polls.developer')),
            ],
        ),
    ]
