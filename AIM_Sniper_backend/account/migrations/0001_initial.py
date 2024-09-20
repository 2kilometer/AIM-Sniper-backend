# Generated by Django 5.1.1 on 2024-09-20 06:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountLoginType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loginType', models.CharField(choices=[('KAKAO', 'Kakao'), ('NORMAL', 'normal'), ('GOOGLE', 'google')], max_length=10, unique=True)),
            ],
            options={
                'db_table': 'account_login_type',
            },
        ),
        migrations.CreateModel(
            name='AccountRoleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roleType', models.CharField(choices=[('ADMIN', 'Admin'), ('NORMAL', 'Normal'), ('BLACKLIST', 'Blacklist')], default='NORMAL', max_length=64, unique=True)),
            ],
            options={
                'db_table': 'account_role_type',
            },
        ),
        migrations.CreateModel(
            name='LoginHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('account_id', models.IntegerField()),
                ('login_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'account_login_history',
            },
        ),
        migrations.CreateModel(
            name='ProfileGenderType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender_type', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], max_length=10, unique=True)),
            ],
            options={
                'db_table': 'profile_gender_type',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('withdraw_reason', models.CharField(choices=[('SERVICE_DISSATISFACTION', 'Service Dissatisfaction'), ('LOW_USAGE', 'Low Usage'), ('OTHER_SERVICE', 'Other Service'), ('PRIVACY_CONCERN', 'Privacy Concern'), ('OTHER', 'Other')], max_length=128, null=True)),
                ('withdraw_at', models.DateTimeField(null=True)),
                ('loginType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.accountlogintype')),
                ('roleType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.accountroletype')),
            ],
            options={
                'db_table': 'account',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=64, unique=True)),
                ('email', models.CharField(max_length=64, unique=True)),
                ('password', models.CharField(default=None, max_length=64, null=True)),
                ('salt', models.CharField(default=None, max_length=16, null=True)),
                ('birthyear', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.profilegendertype')),
            ],
            options={
                'db_table': 'profile',
            },
        ),
    ]
