# Generated by Django 3.2.5 on 2021-07-31 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billsapi', '0003_auto_20210731_0111'),
    ]

    operations = [
        migrations.AddField(
            model_name='billsitems',
            name='negative',
            field=models.BooleanField(default=False),
        ),
    ]
