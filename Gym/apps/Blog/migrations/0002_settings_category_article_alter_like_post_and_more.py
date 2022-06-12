# Generated by Django 4.0.4 on 2022-05-22 11:46

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
            ],
            options={
                'verbose_name': 'تگ',
                'verbose_name_plural': 'نگ ها',
                'db_table': 'T_setting',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='نام دسته بندی')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='آدرس دسته بندی')),
                ('status', models.BooleanField(default=True, verbose_name='آیا نمایش داده شود؟')),
                ('position', models.IntegerField(verbose_name='پوریشن')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='Blog.category', verbose_name='زیردسته')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
                'db_table': 'T_Categores',
                'ordering': ['parent__id', 'position'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان مقاله')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='آدرس مقاله')),
                ('content', ckeditor.fields.RichTextField(verbose_name='متن مقاله')),
                ('img', models.ImageField(upload_to='images/blog', verbose_name='تصویر مقاله')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name=' زمان ایجاد مقاله')),
                ('published_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشارمقاله')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='زمان آپدیت مقاله ')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال/غیرفعال')),
                ('status', models.CharField(choices=[('Draf', 'پیش نویس'), ('Publish', 'منتشر شده')], default='پیش نویس', max_length=10, verbose_name='وضعیت')),
                ('category', models.ManyToManyField(related_name='articles', to='Blog.category', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقالات',
                'db_table': 'T_Article',
                'ordering': ['-published_at'],
            },
        ),
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.article'),
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]