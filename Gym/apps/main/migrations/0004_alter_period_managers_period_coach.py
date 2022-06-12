# Generated by Django 4.0 on 2022-05-04 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_period_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='period',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='period',
            name='coach',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.coach', verbose_name='نام استاد'),
        ),
    ]
