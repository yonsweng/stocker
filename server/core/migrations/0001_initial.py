# Generated by Django 3.0.7 on 2020-06-25 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('count', models.IntegerField()),
            ],
        ),
    ]
