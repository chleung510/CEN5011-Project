# Generated by Django 3.2.9 on 2021-11-15 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=1000)),
            ],
        ),
    ]
