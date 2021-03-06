# Generated by Django 2.2.10 on 2021-08-05 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('fees', models.IntegerField(default=500)),
            ],
        ),
        migrations.CreateModel(
            name='PatientList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('gender', models.CharField(choices=[('1', 'Male'), ('2', 'Female')], max_length=32)),
                ('age', models.IntegerField(max_length=32)),
                ('disease', models.CharField(max_length=32)),
                ('started_meds', models.DateTimeField(blank=True, null=True)),
                ('doctor_con', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.DoctorList')),
            ],
        ),
    ]
