# Generated by Django 3.0.1 on 2019-12-29 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DistributorInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distributor_name', models.CharField(max_length=35)),
                ('distributor_type', models.CharField(choices=[('Distributor', 'Distributor'), ('Supermarkets', 'Supermarkets'), ('Food & Restaurent', 'Food & Restaurent')], max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Distributor Information',
                'verbose_name_plural': 'Distributor Informations',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30, unique=True)),
                ('user_type', models.CharField(max_length=10)),
                ('user_full_name', models.CharField(max_length=80)),
                ('user_email', models.CharField(max_length=80, unique=True)),
                ('user_password', models.CharField(max_length=150)),
                ('user_mobile', models.CharField(max_length=15)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'User List',
                'verbose_name_plural': 'User Lists',
            },
        ),
        migrations.CreateModel(
            name='InspectionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.BigIntegerField(default=0)),
                ('action_taken', models.CharField(blank=True, max_length=30, null=True)),
                ('option_one', models.BooleanField(default=False)),
                ('option_one_img', models.ImageField(blank=True, upload_to='inspection_img')),
                ('option_two', models.BooleanField(default=False)),
                ('option_two_img', models.ImageField(blank=True, upload_to='inspection_img')),
                ('option_three', models.BooleanField(default=False)),
                ('option_three_img', models.ImageField(blank=True, upload_to='inspection_img')),
                ('option_four', models.BooleanField(default=False)),
                ('option_four_img', models.ImageField(blank=True, upload_to='inspection_img')),
                ('option_five', models.BooleanField(default=False)),
                ('option_five_img', models.ImageField(blank=True, upload_to='inspection_img')),
                ('option_six', models.BooleanField(default=False)),
                ('option_six_img', models.ImageField(blank=True, upload_to='inspection_img')),
                ('fine_amount', models.FloatField(default=0)),
                ('issue_warning', models.CharField(blank=True, max_length=30, null=True)),
                ('inspection_date', models.DateTimeField()),
                ('inserted_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('distributor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.DistributorInfo')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.UserInfo')),
            ],
            options={
                'verbose_name': 'Inspection Information',
                'verbose_name_plural': 'Inspection Informations',
            },
        ),
    ]