# Generated by Django 3.2.9 on 2021-11-15 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211114_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='notice',
            name='noticeID',
            field=models.CharField(max_length=10),
        ),
    ]
