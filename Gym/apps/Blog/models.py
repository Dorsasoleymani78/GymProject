 
 
from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from extensions.utils import jalali_converter
from apps.account.models import User
from django.urls import reverse
# models manager
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='Publish')
    
class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)
      
# Create your models here.
class Category(models.Model):
    parent=models.ForeignKey('self',on_delete=models.SET_NULL,verbose_name='زیردسته',related_name='children',blank=True,null=True)
    title=models.CharField(max_length=50,verbose_name='نام دسته بندی' )
    slug=models.SlugField(max_length=100,unique=True,verbose_name='آدرس دسته بندی')
    status=models.BooleanField(default=True,verbose_name='آیا نمایش داده شود؟')
    position=models.IntegerField(verbose_name='پوریشن') 
    objects=CategoryManager()
     
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name='دسته بندی'
        verbose_name_plural= 'دسته بندی ها'
        db_table='T_Categores' 
        ordering=['parent__id','position']
        
class Article(models.Model):
    STATUS_CHOISES=(('Draf','پیش نویس'),('Publish','منتشر شده'))
    title=models.CharField(max_length=100,verbose_name='عنوان مقاله')
    slug=models.SlugField(max_length=100,unique=True,verbose_name='آدرس مقاله')
    category=models.ManyToManyField(Category,  verbose_name='دسته بندی',related_name='articles')
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='articles',null=True,verbose_name='نویسنده')
    content=RichTextField(verbose_name='متن مقاله')
    img=models.ImageField(upload_to='images/blog',verbose_name='تصویر مقاله')
    create_at=models.DateTimeField(auto_now_add=True,null=True,blank=True,verbose_name=' زمان ایجاد مقاله')
    published_at=models.DateTimeField(default=timezone.now,verbose_name='زمان انتشارمقاله')
    update_at=models.DateTimeField(auto_now=True,verbose_name='زمان آپدیت مقاله ')
    is_active=models.BooleanField(default=False,verbose_name='فعال/غیرفعال')
    status=models.CharField(max_length=10,choices=STATUS_CHOISES,verbose_name='وضعیت',default='پیش نویس')
  
    def __str__(self) -> str:
        return  self.title 
    
    def get_absolute_url(self):
        return reverse("account:home")
    
    
    def j_publish(self):
        return jalali_converter(self.published_at)
    
    j_publish.short_description='زمان انتشار'
    
    def j_update(self):
        return jalali_converter(self.update_at)
    j_update.short_description='زمان آپدیت'
    
    def category_to_str(self ):
        return ",".join([item.title for item in self.category.active()])
    
    category_to_str.short_description='دسته بندی'

    
    objects=ArticleManager()
    
    
    class Meta:
        verbose_name='مقاله'
        verbose_name_plural= 'مقالات'
        db_table='T_Article'
        ordering=['-published_at']
    
class like(models.Model):
    post=models.ForeignKey(Article,on_delete=models.CASCADE)
    
class settings(models.Model):
    title=models.CharField(max_length=100,verbose_name='عنوان')
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name='تگ'
        verbose_name_plural= 'نگ ها'
        db_table='T_setting'
 
    
    