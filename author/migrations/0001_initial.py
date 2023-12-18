# Generated by Django 4.1.12 on 2023-12-18 08:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('author_name', models.CharField(max_length=225)),
                ('author_email', models.EmailField(max_length=225)),
                ('author_number', models.CharField(max_length=10)),
                ('birth_date', models.DateField()),
                ('death_date', models.DateField()),
                ('country', models.CharField(max_length=225)),
                ('bio', models.CharField(max_length=500)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50)),
            ],
        ),
    ]