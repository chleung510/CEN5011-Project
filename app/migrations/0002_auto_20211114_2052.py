# Generated by Django 3.2.9 on 2021-11-15 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='id',
        ),
        migrations.AddField(
            model_name='notice',
            name='noticeID',
            field=models.AutoField(default='0000000', primary_key=True, serialize=False),
        ),
    ]
