# Generated by Django 2.2.6 on 2021-06-22 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20210621_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='users',
            field=models.CharField(default='', max_length=12),
        ),
    ]