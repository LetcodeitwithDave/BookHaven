# Generated by Django 4.2.10 on 2024-03-04 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0028_alter_message_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='number',
            field=models.BigIntegerField(),
        ),
    ]
