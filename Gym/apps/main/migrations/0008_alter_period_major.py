# Generated by Django 4.0.4 on 2022-05-05 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='major',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.major', verbose_name='نام رشته'),
        ),
    ]
