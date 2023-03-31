# Generated by Django 4.1.7 on 2023-03-25 16:20

import apps.validators.booking_validators
import apps.validators.customer_validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('booking_confirmed', models.BooleanField(default=False)),
                ('booking_date', models.DateField(validators=[apps.validators.booking_validators.booking_date_validator])),
                ('booking_time', models.TimeField(validators=[apps.validators.booking_validators.booking_time_validator])),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('message', models.TextField(blank=True, max_length=500, validators=[apps.validators.customer_validators.validate_message])),
                ('placements', models.PositiveSmallIntegerField(default=1, validators=[apps.validators.booking_validators.booking_placement_validator])),
            ],
        ),
    ]
