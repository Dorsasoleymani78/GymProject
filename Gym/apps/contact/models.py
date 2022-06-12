 
# from enum import unique
# import imp
# from django.db import models
# from django.db.models import F
# # Create your models here.
# from django.core import validators
# # from apps.main.models import eriod
# from ..main.validation import *
 
# Create your models here.
#ورزشکار

   
# class athlete(models.Model):
#     name=models.CharField(max_length=20,verbose_name='نام',validators=[validate_name])
#     family=models.CharField(max_length=20,verbose_name='نام خانوادگی',validators=[validate_name]) 
#     age=models.IntegerField(verbose_name='سن',default=0,validators=[validators.MaxValueValidator(40,message='Age can not be more than 40'),validators.MinValueValidator(5,message='Age can not be less than 5')]) 
#     Address=models.TextField(max_length=200,verbose_name='آدرس',validators=[validate_Address])
#     GendesType=[('Man','مرد'),('Female','زن')]
#     Gender=models.CharField(max_length=40,choices=GendesType,verbose_name='جنسیت')
#     phone_number = models.CharField(  max_length=17, blank=True) # Validators should be a list
#     slug=models.SlugField(max_length=100)
  
#     gad=models.IntegerField(verbose_name='قد',null=True)
#     vazn=models.IntegerField(verbose_name='وزن',null=True )
   
#     def sabt_barname(self):
#         if (self.gad>=150 and self.gad<=160) and (self.vazn>=50 and self.vazn<=60):
#             tamrin='هرروز دراز نشست'
#             tagziye='روزی یک قرص نان'
            
#         elif (self.gad<=160 and self.gad<=170) and (self.vazn>=50 and self.vazn<=60):
#             tamrin= 'هرروز 30 دقیقه بدو'
#             tagziye= 'هرروز یک موز'
#         else:
#             tamrin='اوکی'
#             tagziye='ااا'
#         return f' {tamrin} \n   {tagziye}' 
#     description=property(sabt_barname)
#     description.fget.short_description='برنامه تغزی '
    
#     def __str__(self) -> str:
#         return  self.name+'\t'+self.family+'\t'+str(self.age)
    
#     def Check_Athlete_Type(self ):
#         val=int(self.age)
#         if val>=11 and val<=18:
#             return 'نوجوان'
#         elif val>=19 and val<=35:
#             return 'جوان'
#         elif val>=36:
#             return 'میان سال'
        
#     athlete_Type= property(Check_Athlete_Type)
#     athlete_Type.fget.short_description ='نام نوع ورزشکار'
    
    
#     class Meta:
#         verbose_name='ورزشکار'
#         verbose_name_plural= 'ورزشکار ها'
#         db_table='T_athlete'

      
 