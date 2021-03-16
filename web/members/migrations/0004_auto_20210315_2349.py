# Generated by Django 2.2.7 on 2021-03-15 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_scoreofbloodtype_scoreofdaysofweek_scoreofnaksus_scoreofrasi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scoreofbloodtype',
            name='memberA',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bloodType_pk_req', to='members.BloodType'),
        ),
        migrations.AlterField(
            model_name='scoreofbloodtype',
            name='memberB',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bloodType_pk_all', to='members.BloodType'),
        ),
    ]
