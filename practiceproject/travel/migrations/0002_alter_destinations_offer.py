# Generated by Django 5.0.3 on 2024-03-07 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destinations',
            name='offer',
            field=models.BooleanField(default=False),
        ),
    ]
