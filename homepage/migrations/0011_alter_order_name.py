# Generated by Django 4.2.5 on 2024-02-04 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0010_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=230),
        ),
    ]
