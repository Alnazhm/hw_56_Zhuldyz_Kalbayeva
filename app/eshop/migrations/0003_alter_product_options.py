# Generated by Django 4.1.1 on 2022-10-04 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0002_product_deleted_at_product_is_deleted'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['category', 'title'], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]