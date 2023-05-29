# Generated by Django 4.2.1 on 2023-05-29 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_order_items_item_order_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('await', 'Awaiting'), ('completed', 'Completed')], default='await', max_length=10),
        ),
    ]
