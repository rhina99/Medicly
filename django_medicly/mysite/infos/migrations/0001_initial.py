# Generated by Django 2.1.5 on 2019-03-03 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=30)),
                ('LastName', models.CharField(max_length=30)),
                ('Gender', models.BooleanField()),
                ('purchase_date', models.DateTimeField()),
                ('Age', models.BigIntegerField(max_length=3)),
                ('HospNumb', models.BigIntegerField(max_length=12)),
            ],
        ),
    ]