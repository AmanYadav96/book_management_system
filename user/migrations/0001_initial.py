# Generated by Django 4.1.12 on 2023-12-21 07:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user_email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('user_name', models.CharField(max_length=255)),
                ('user_password', models.CharField(max_length=255)),
                ('user_number', models.CharField(max_length=10)),
                ('user_role', models.CharField(max_length=225)),
                ('is_verify', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
