# Generated by Django 2.2.7 on 2021-01-11 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bloodtype', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'หมู่เลือด',
            },
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, null=True)),
                ('block', models.BooleanField(blank=True, default=False, null=True)),
                ('rejected', models.BooleanField(blank=True, default=False, null=True)),
                ('reviewe_value', models.IntegerField(blank=True, null=True)),
                ('joined_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'สนทนา',
            },
        ),
        migrations.CreateModel(
            name='DaysOfWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daysofweek', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'วันประจำวันเกิด',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'เพศ',
            },
        ),
        migrations.CreateModel(
            name='NakSus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naksus', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'นักษัตร',
            },
        ),
        migrations.CreateModel(
            name='RaSi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasi', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'ราศี',
            },
        ),
        migrations.CreateModel(
            name='Testes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testes', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'รสนิยมทางเพศ',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=564)),
                ('password', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('birthday', models.DateField()),
                ('age', models.IntegerField()),
                ('profileurl', models.TextField(blank=True, default='', null=True)),
                ('discription', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('characterneed', models.IntegerField()),
                ('values', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('bloodtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.BloodType', verbose_name='หมู่เลือด')),
                ('dayofbirth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.DaysOfWeek', verbose_name='วันประจำวันเกิด')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Gender', verbose_name='เพศ')),
                ('naksus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.NakSus', verbose_name='นักษัตร')),
                ('rasi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.RaSi', verbose_name='ราศีประจำวันเกิด')),
                ('testes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Testes', verbose_name='รสนิยมทางเพศ')),
            ],
        ),
        migrations.CreateModel(
            name='Goldmember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Conversation', verbose_name='id Conversatios')),
                ('goldmember', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Member', verbose_name='id')),
            ],
        ),
        migrations.AddField(
            model_name='conversation',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Member'),
        ),
    ]
