# Generated by Django 3.1.1 on 2020-11-18 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('release_date', models.DateTimeField(verbose_name='Date Released')),
                ('discount_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('current_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('platform', models.CharField(max_length=20)),
                ('launcher', models.CharField(max_length=20)),
                ('savings_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('developer', models.CharField(max_length=30)),
                ('publisher', models.CharField(max_length=30)),
            ],
        ),
    ]
