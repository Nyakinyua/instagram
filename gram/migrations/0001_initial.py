# Generated by Django 2.2.4 on 2019-12-27 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('bio', models.TextField(max_length=200)),
                ('profile_photo', models.ImageField(blank=True, upload_to='profile/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('image_name', models.CharField(max_length=30)),
                ('caption', models.CharField(max_length=100)),
                ('posted_on', models.DateField(auto_now_add=True)),
                ('comment', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gram.Comment')),
                ('like', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gram.Like')),
                ('profile', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gram.Profile')),
            ],
            options={
                'ordering': ['posted_on'],
            },
        ),
    ]
