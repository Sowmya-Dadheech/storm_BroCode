# Generated by Django 4.2.4 on 2023-10-04 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_product_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='author',
        ),
        migrations.RemoveField(
            model_name='product',
            name='title',
        ),
    ]
