# Generated by Django 3.0 on 2019-12-15 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20191215_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='file_name',
            field=models.CharField(default='temp', max_length=200),
        ),
    ]
