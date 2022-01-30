# Generated by Django 4.0.1 on 2022-01-30 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astro', '0002_event_imgurls'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('Blog_id', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=500)),
                ('headimg', models.TextField()),
                ('Discription', models.TextField()),
                ('Author', models.TextField(default='')),
                ('R1', models.TextField(default='')),
                ('R2', models.TextField(default='')),
            ],
        ),
    ]
