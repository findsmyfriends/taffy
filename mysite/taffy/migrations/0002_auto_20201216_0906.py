# Generated by Django 3.1.4 on 2020-12-16 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taffy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('birth', models.DateField(auto_now=True)),
                ('discription', models.CharField(default='', max_length=1000)),
                ('sexual', models.CharField(max_length=100)),
                ('sextest', models.CharField(max_length=100)),
                ('link_pic', models.TextField(blank=True, default='')),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Prfiles',
        ),
    ]
