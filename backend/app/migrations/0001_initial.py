# Generated by Django 5.0.2 on 2024-02-08 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=200)),
                ('idade', models.IntegerField()),
            ],
        ),
    ]
