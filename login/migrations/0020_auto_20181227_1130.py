# Generated by Django 2.1.4 on 2018-12-27 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0019_auto_20181227_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='purchase_price',
            field=models.CharField(max_length=10),
        ),
    ]