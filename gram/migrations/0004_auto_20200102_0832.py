# Generated by Django 2.2.4 on 2020-01-02 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0003_auto_20191231_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='image_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gram.Images'),
        ),
        migrations.AddField(
            model_name='comment',
            name='images',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='images',
            name='like',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='gram.Like'),
        ),
    ]
