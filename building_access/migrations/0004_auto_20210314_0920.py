# Generated by Django 3.1.5 on 2021-03-14 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building_access', '0003_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_name',
            field=models.CharField(max_length=128),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
