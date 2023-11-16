# Generated by Django 4.2 on 2023-11-16 13:15

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('gender', models.CharField(choices=[('MALE', 'male'), ('FEMALE', 'female'), ('OTHER', 'other')], default='FEMALE', max_length=50)),
                ('birth_date', models.DateField()),
                ('phone', phone_field.models.PhoneField(max_length=31)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('national_id', models.CharField(max_length=100)),
                ('specialization', models.CharField(choices=[('Allergology&Immunology', 'Allergology&Immunology'), ('Infectious_diseases', 'Infectious_diseases'), ('Dermatology', 'Dermatology'), ('Internal_Medicine', 'Internal_Medicine'), ('Endocrinology', 'Endocrinology'), ('Gastroenterology', 'Gastroenterology'), ('Geriatrics', 'Geriatrics'), ('Hematology', 'Hematology'), ('Cardiology', 'Cardiology'), ('Cancer_Medicine', 'Cancer_Medicine'), ('Clinical_Psychology', 'Clinical_Psychology'), ('Nephrology', 'Nephrology'), ('Neurophysiopathology', 'Neurophysiopathology'), ('Neurology', 'Neurology'), ('Paediatrics', 'Paediatrics'), ('Pediatric_Psychiatry', 'Pediatric_Psychiatry'), ('Sports_Medicine', 'Sports_Medicine'), ('Tropical_Medicine', 'Tropical_Medicine')], default='Allergology&Immunology', max_length=50)),
                ('medical_council_code', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HealthInsurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('phone', phone_field.models.PhoneField(max_length=31)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('discount_percentage', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('gender', models.CharField(choices=[('MALE', 'male'), ('FEMALE', 'female'), ('OTHER', 'other')], default='FEMALE', max_length=50)),
                ('birth_date', models.DateField()),
                ('phone', phone_field.models.PhoneField(max_length=31)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('national_id', models.CharField(max_length=100)),
                ('patient_id', models.IntegerField(primary_key=True, serialize=False)),
                ('health_insurance_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='hospital.healthinsurance')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PatientHistory',
            fields=[
                ('date', models.DateTimeField()),
                ('diagnosis', models.TextField()),
                ('prescription', models.TextField()),
                ('drug_used', models.TextField(blank=True)),
                ('note', models.TextField(blank=True)),
                ('patient_history_id', models.IntegerField(primary_key=True, serialize=False)),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctor')),
                ('patient_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hospital.patient')),
            ],
        ),
        migrations.CreateModel(
            name='PatientBill',
            fields=[
                ('patient_bill_id', models.IntegerField(primary_key=True, serialize=False)),
                ('total_cost', models.FloatField()),
                ('date', models.DateTimeField()),
                ('insurance_contribution', models.FloatField()),
                ('transaction_status', models.BooleanField(default=False)),
                ('patient_history_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patienthistory')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('reason', models.TextField()),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment', to='hospital.doctor')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointment', to='hospital.patient')),
            ],
        ),
    ]
