# Generated by Django 2.2.6 on 2021-06-22 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mydata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='', max_length=20)),
                ('job_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Mypostjob',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('position', models.CharField(max_length=50)),
                ('company', models.CharField(default='', max_length=500)),
                ('experience', models.CharField(default='', max_length=5000)),
                ('package', models.CharField(default='', max_length=500)),
                ('location', models.CharField(default='', max_length=500)),
                ('skill', models.CharField(default='', max_length=500)),
                ('desc', models.CharField(default='', max_length=5000)),
                ('pub_date', models.DateField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]