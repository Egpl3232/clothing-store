# Generated by Django 4.1.7 on 2023-04-11 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_rename_total_amount_order_total_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productinorder',
            old_name='nmb',
            new_name='col_vo',
        ),
    ]
