# Generated by Django 5.0.1 on 2024-04-01 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_subpackage_member_cartitem_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='p_days',
            field=models.IntegerField(default=7),
        ),
    ]
