# Generated by Django 3.0.5 on 2021-01-05 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building_access', '0002_remove_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]