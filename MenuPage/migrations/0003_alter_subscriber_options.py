# Generated by Django 4.1.7 on 2023-04-13 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MenuPage', '0002_rename_subscribers_subscriber'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscriber',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]
