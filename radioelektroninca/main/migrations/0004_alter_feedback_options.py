# Generated by Django 4.2.3 on 2023-08-12 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_feedback_alter_order_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name': 'Рекоментация', 'verbose_name_plural': 'Рекомендации'},
        ),
    ]
