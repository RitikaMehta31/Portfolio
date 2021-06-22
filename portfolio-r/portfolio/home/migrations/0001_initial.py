# Generated by Django 3.1.2 on 2020-10-18 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField(max_length=125)),
                ('image', models.ImageField(blank=True, null=True, upload_to='project/images')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
