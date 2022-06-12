# Generated by Django 4.0.4 on 2022-04-15 14:03

import apps.main.validation
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CoachName', models.CharField(max_length=10, validators=[apps.main.validation.validate_name], verbose_name='نام')),
                ('CoachFamily', models.CharField(max_length=10, verbose_name='نام خانوادگی ')),
                ('Address', models.TextField(max_length=200, validators=[apps.main.validation.validate_Address], verbose_name='آدرس')),
                ('Gender', models.CharField(choices=[('Man', 'مرد'), ('Female', 'زن')], max_length=40, verbose_name='جنسیت')),
                ('phone_number', models.CharField(blank=True, max_length=17)),
            ],
            options={
                'verbose_name': 'مربی',
                'verbose_name_plural': 'مربیان',
                'db_table': 'T_Coach',
            },
        ),
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GymName', models.CharField(max_length=10, validators=[apps.main.validation.validate_name], verbose_name='نام باشگاه')),
                ('Address', models.TextField(max_length=200, validators=[apps.main.validation.validate_Address], verbose_name='آدرس')),
            ],
            options={
                'verbose_name': 'باشگاه',
                'verbose_name_plural': 'باشگاه ها',
                'db_table': 'T_Gym',
            },
        ),
        migrations.CreateModel(
            name='major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('majorName', models.CharField(max_length=10, validators=[apps.main.validation.validate_name], verbose_name='نام رشته')),
                ('TypeOfMajor', models.CharField(choices=[('ورزش های حرکتی', 'ورزش های حرکتی'), ('ورزش های نمایشی', 'ورزش های نمایشی'), ('ورزش های رزمی', 'ورزش های رزمی'), ('ورزش های قدرتی', 'ورزش های قدرتی'), ('ورزش های ماجراجویانه', 'ورزش های ماجراجویانه'), ('ورزش های سواری', 'ورزش های سواری'), (' ورزش\u200cهای نشانه\u200cروی', ' ورزش\u200cهای نشانه\u200cروی'), ('ورزش\u200cهای گروهی', 'ورزش\u200cهای گروهی'), (' ورزش\u200cهای راکتی', ' ورزش\u200cهای راکتی'), (' ورزش\u200cهای فکری', ' ورزش\u200cهای فکری'), (' ورزش\u200cهای ساحلی', 'ورزش\u200cهای ساحلی'), (' ورزش\u200cهای آبی', 'ورزش\u200cهای آبی'), ('ورزش\u200cهای هوایی', 'ورزش\u200cهای هوایی')], default='ورزش های حرکتی', max_length=50, verbose_name='نوع رشته ورزشی')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال/غیرفعال')),
            ],
            options={
                'verbose_name': 'رشته',
                'verbose_name_plural': 'رشته ها',
                'db_table': 'T_major',
            },
        ),
        migrations.CreateModel(
            name='salon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SalonName', models.CharField(max_length=10, validators=[apps.main.validation.validate_name], verbose_name='نام سالن')),
                ('Capacity', models.IntegerField(default=0, validators=[apps.main.validation.validate_Capacity], verbose_name='ظرفیت')),
                ('Is_Active', models.BooleanField(default=False, verbose_name='فعال/غیرفعال')),
            ],
            options={
                'verbose_name': 'سالن',
                'verbose_name_plural': 'سالن ها',
                'db_table': 'T_salon',
            },
        ),
        migrations.CreateModel(
            name='TypePriod',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='کد نوع دوره')),
                ('title', models.CharField(max_length=10, verbose_name='نوع دوره')),
            ],
            options={
                'verbose_name': 'نوع دوره',
                'verbose_name_plural': 'انواع',
                'db_table': 'T_TypePriod',
            },
        ),
        migrations.CreateModel(
            name='period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField(default=0, verbose_name='شهریه')),
                ('Capacity', models.IntegerField(default=0, verbose_name='ظرفیت')),
                ('startDate_at', models.DateField(verbose_name='تاریخ شروع')),
                ('timestarted_at', models.TimeField(verbose_name='زمان شروع')),
                ('timeended_at', models.TimeField(verbose_name='زمان پایان')),
                ('coach', models.ForeignKey(default='coach', on_delete=django.db.models.deletion.CASCADE, to='main.coach', verbose_name='نام استاد')),
                ('majorName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.major', verbose_name='نام رشته')),
                ('salon', models.ForeignKey(default='salon', on_delete=django.db.models.deletion.CASCADE, to='main.salon', verbose_name='سالن')),
                ('typeOfPeriod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.typepriod', verbose_name='نوع دوره')),
            ],
            options={
                'verbose_name': 'دوره',
                'verbose_name_plural': 'دوره ها',
                'db_table': 'T_period',
            },
        ),
        migrations.AddField(
            model_name='coach',
            name='majorName',
            field=models.ManyToManyField(to='main.major', verbose_name='نام رشته '),
        ),
    ]
