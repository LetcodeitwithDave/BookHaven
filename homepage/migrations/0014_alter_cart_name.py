# Generated by Django 4.2.5 on 2024-02-05 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0013_alter_cart_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
