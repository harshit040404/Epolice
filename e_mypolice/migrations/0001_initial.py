# Generated by Django 4.1 on 2022-08-15 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.BigIntegerField()),
                ('email_id', models.EmailField(max_length=254)),
                ('msg', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='login_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('email_id', models.EmailField(max_length=254)),
                ('passwrd', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
            ],
        ),
    ]