# Generated by Django 4.2.1 on 2023-05-29 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.JSONField(default=dict),
        ),
    ]
