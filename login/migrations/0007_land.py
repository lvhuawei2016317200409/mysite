# Generated by Django 2.1.4 on 2018-12-25 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_remove_user_sex'),
    ]

    operations = [
        migrations.CreateModel(
            name='Land',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone', models.CharField(max_length=32)),
                ('landmark', models.CharField(max_length=32)),
                ('lot', models.CharField(max_length=32)),
                ('position', models.CharField(max_length=32)),
                ('area', models.CharField(max_length=128)),
            ],
        ),
    ]
