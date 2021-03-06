# Generated by Django 2.1.2 on 2018-10-25 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_Id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('pswd', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=12)),
                ('email', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
            ],
        ),
    ]
