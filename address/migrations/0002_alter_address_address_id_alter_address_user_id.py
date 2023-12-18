# Generated by Django 4.1.12 on 2023-12-18 08:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '__first__'),
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_id',
            field=models.UUIDField(default=uuid.UUID('f872b130-0dbb-41ef-9c22-93786fc4a5a3'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='address',
            name='user_id',
            field=models.ForeignKey(default=uuid.UUID('baa7a892-1f3e-4dc7-b397-582894920310'), on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]
