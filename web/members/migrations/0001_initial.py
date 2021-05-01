# Generated by Django 2.2.7 on 2021-04-30 11:37

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import members.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('description', models.TextField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='F', max_length=1)),
                ('testes', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='M', max_length=1)),
                ('profile_image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('birthday', models.DateField(blank=True, default=datetime.date(1998, 3, 11), null=True)),
            ],
            options={
                'verbose_name': 'Member',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='BloodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bloodtype', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DaysOfWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daysofweek', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NakSus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naksus', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RaSi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasi', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ScoreRaSi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scorerasi', models.IntegerField()),
                ('rasiA', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rasi1', to='members.RaSi')),
                ('rasiB', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rasi2', to='members.RaSi')),
            ],
        ),
        migrations.CreateModel(
            name='ScoreNakSus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scorenaksus', models.IntegerField()),
                ('naksusA', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='naksus1', to='members.NakSus')),
                ('naksusB', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='naksus2', to='members.NakSus')),
            ],
        ),
        migrations.CreateModel(
            name='ScoreDaysOfWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scoredaysofweek', models.IntegerField()),
                ('daysofweekA', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='daysofweek1', to='members.DaysOfWeek')),
                ('daysofweekB', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='daysofweek2', to='members.DaysOfWeek')),
            ],
        ),
        migrations.CreateModel(
            name='ScoreBloodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scorebloodtype', models.IntegerField(blank=True, null=True)),
                ('bloodtypeA', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bloodtype1', to='members.BloodType')),
                ('bloodtypeB', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bloodtypeB', to='members.BloodType')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(blank=True, null=True)),
                ('profile_score', models.IntegerField(default=5)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('bloodtype', models.ForeignKey(default=members.models.get_bloodtype, on_delete=django.db.models.deletion.CASCADE, to='members.BloodType', verbose_name='หมู่เลือด')),
                ('daysofweek', models.ForeignKey(default=members.models.get_daysofweek, on_delete=django.db.models.deletion.CASCADE, to='members.DaysOfWeek', verbose_name='วันประจำวันเกิด')),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('naksus', models.ForeignKey(default=members.models.get_naksus, on_delete=django.db.models.deletion.CASCADE, to='members.NakSus', verbose_name='นักษัตร')),
                ('rasi', models.ForeignKey(default=members.models.get_rasi, on_delete=django.db.models.deletion.CASCADE, to='members.RaSi', verbose_name='ราศี')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='bloodtype',
            field=models.ForeignKey(blank=True, default=3, null=True, on_delete=django.db.models.deletion.CASCADE, to='members.BloodType', verbose_name='หมู่เลือด'),
        ),
        migrations.AddField(
            model_name='member',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='member',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratingPoint', models.IntegerField(blank=True, null=True)),
                ('member_excluded', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_excluded', to='members.Profile')),
                ('member_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_owner', to='members.Profile')),
            ],
            options={
                'unique_together': {('member_owner', 'member_excluded')},
            },
        ),
        migrations.CreateModel(
            name='NoMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(blank=True, null=True)),
                ('nomatcher_excluded', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nomatcher_excluded', to='members.Profile')),
                ('nomatcher_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nomatcher_owner', to='members.Profile')),
            ],
            options={
                'unique_together': {('nomatcher_excluded', 'nomatcher_owner')},
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(blank=True, null=True)),
                ('matcher_excluded', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matcher_excluded', to='members.Profile')),
                ('matcher_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matcher_owner', to='members.Profile')),
            ],
            options={
                'unique_together': {('matcher_excluded', 'matcher_owner')},
            },
        ),
    ]
