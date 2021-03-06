# Generated by Django 2.1.2 on 2018-10-27 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_driver'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cab',
            fields=[
                ('cab_Id', models.AutoField(primary_key=True, serialize=False)),
                ('lisence', models.CharField(max_length=15)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CabRideStatus',
            fields=[
                ('cabRideStatus_Id', models.BooleanField(primary_key=True, serialize=False)),
                ('cabRideStatus_Name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('carModel_Id', models.AutoField(primary_key=True, serialize=False)),
                ('modelName', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentOption',
            fields=[
                ('paymentOption_Id', models.AutoField(primary_key=True, serialize=False)),
                ('paymentOption_Name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='cab',
            name='carModel_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.CarModel'),
        ),
        migrations.AddField(
            model_name='cab',
            name='driver_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.Driver'),
        ),
    ]
