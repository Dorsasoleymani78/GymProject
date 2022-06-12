 
 
from statistics import mode
from turtle import position
from django.db import models

# Create your models here.
 
from django.db import models
from django.db.models import F
# Create your models here.
from .validation import *
# from apps.contact.models import athlete
 
# Create your models here.
class salon(models.Model):
 
    SalonName=models.CharField(max_length=10,verbose_name='نام سالن',validators=[validate_name])
    Capacity=models.IntegerField(default=0,verbose_name='ظرفیت',validators=[validate_Capacity])
    Is_Active=models.BooleanField(default=False,verbose_name='فعال/غیرفعال')
 
    def __str__(self) -> str:
        return self.SalonName
    
 
    def save(self,*args,**kwargs) -> None:
        self.full_clean()
        return super().save(*args,**kwargs)
    
    class Meta:
        verbose_name='سالن'
        verbose_name_plural= 'سالن ها'
        db_table='T_salon'
#category for majorGroups
class majorGroups(models.Model):
    id=models.IntegerField(primary_key=True )
    title=models.CharField(max_length=50,verbose_name='نام گروه ورزشی' )
 
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name='گروه ورزشی'
        verbose_name_plural= 'گروه های ورزشی'
        db_table='T_ majorGroups' 
 
        
class Major(models.Model):
    majorName=models.CharField(max_length=30,verbose_name='نام رشته',blank=True)
    MajorGroup=models.ForeignKey( majorGroups,on_delete=models.CASCADE,verbose_name='نوع رشته ورزشی',null=True )
    is_active=models.BooleanField( verbose_name='فعال/غیرفعال',null=True)
 
    
    def __str__(self) :
        return  str(self.majorName ) 
    
    def save(self,*args,**kwargs) -> None:
        self.full_clean()
        return super().save(*args,**kwargs)

    class Meta:
        verbose_name='رشته'
        verbose_name_plural= 'رشته ها'
        db_table='T_major'
        
class Coach(models.Model):
    CoachName=models.CharField(max_length=10,verbose_name='نام',validators=[validate_name],blank=True)
    CoachFamily=models.CharField(max_length=20,verbose_name='نام خانوادگی ',blank=True)
    Address=models.TextField(max_length=200,verbose_name='آدرس',validators=[validate_Address],blank=True)
    GendesType=[('Man','مرد'),('Female','زن')]
    Gender=models.CharField(max_length=40,choices=GendesType,verbose_name='جنسیت',blank=True)
    phone_number = models.CharField( max_length=17, blank=True,verbose_name='تلفن' )  
    majorName=models.ManyToManyField(Major,verbose_name='نام رشته ',blank=True  )

    def __str__(self) :
        return  str(self.CoachName) 
    
    def save(self,*args,**kwargs) -> None:
        self.full_clean()
        return super().save(*args,**kwargs)
    
    class Meta:
        verbose_name='مربی'
        verbose_name_plural= 'مربیان'
        db_table='T_Coach'
        
class Gym(models.Model):
    GymName=models.CharField(max_length=10,verbose_name='نام باشگاه',validators=[validate_name])
    Address=models.TextField(max_length=200,verbose_name='آدرس',validators=[validate_Address])
 
    
    def __str__(self) -> str:
        return  self.GymName 
    
    def save(self,*args,**kwargs) -> None:
        self.full_clean()
        return super().save(*args,**kwargs)
    
    class Meta:
        verbose_name='باشگاه'
        verbose_name_plural= 'باشگاه ها'
        db_table='T_Gym'
        
class TypePriod(models.Model):
    id=models.IntegerField(primary_key=True,verbose_name='کد نوع دوره')
    title=models.CharField(verbose_name='نوع دوره',max_length=10)   
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name='نوع دوره'
        verbose_name_plural='نوع دوره ها'
        db_table='T_TypePriod'
 
     
 
class Period(models.Model):
    periodName=models.CharField(max_length=100,verbose_name='نام دوره',null=True)
    major=models.ForeignKey(Major,verbose_name='نام رشته',on_delete=models.CASCADE,blank=True,null=True)
    typeOfPeriod=models.ForeignKey(TypePriod,verbose_name='نوع دوره',on_delete=models.CASCADE,blank=True,null=True   )
    salon=models.ForeignKey(salon,on_delete=models.CASCADE,verbose_name='سالن',default='salon'  )
    coach=models.ForeignKey(Coach,on_delete=models.CASCADE,null=True,verbose_name='نام استاد')
    salary=models.IntegerField( default=0,verbose_name='شهریه' )
    Capacity=models.IntegerField(default=0,verbose_name='ظرفیت')
    startDate_at=models.DateField(verbose_name='تاریخ شروع')
    timestarted_at=models.TimeField(verbose_name='زمان شروع')
    timeended_at=models.TimeField(verbose_name='زمان پایان')
    is_active=models.BooleanField(default=False,null=True,verbose_name='غیرفعال/فعال')
    def __str__(self) -> str:
        return str(self.major
                   ) 
        
    # def get_major():
    #         field_name = 'salary'
    #         obj = Period.objects.first()
    #         field_object = Period._meta.get_field(field_name)
    #         field_value = getattr(obj, field_object.attname)
    #         return field_value
   
    def get_major(self):
        # try:
        return self.major
            # return Coach.objects.filter(majorName__majorName=self.major.majorName)
        # except:
        #     return self.major.majorName

    # @property
    # def calculated_field(self):
        
    #     return self._do_calculation(self.salary)   
    
    # def save(self, *args, **kwargs):
    #     self.coach=Coach.objects.filter(majorName__majorName=self.majorName.majorName)
        # self.coach= list(p)
       
        # super(Period, self).save(*args, **kwargs)
        
    # def __hash__(self) -> int:
    #     return hash(self.salary)
    def save(self,*args,**kwargs) -> None:
        self.full_clean()
        return super().save(*args,**kwargs)
    
    # def get_coach(self):
    #     # p=Period.objects.filter(coach__majorName=self.majorName.majorName)
    #     # p=Period.objects.filter(coach__CoachName=Coach.objects.filter(majorName__majorName=self.majorName.majorName))
    #     p=Coach.objects.filter(majorName__majorName=self.majorName.majorName)
    #     return list(p)
  
  
    class Meta:
        verbose_name='دوره'
        verbose_name_plural= 'دوره ها'
        db_table='T_period'
        # Coach.objects.filter(period_majormajorname = major_majorname)
        # (coach__majorName__majorName='تکواندو')
       # constraints=[models.CheckConstraint(check=models.Q(coach__majorName='تکواندو'),name='coach__majorName_تکواندو')]
       # UniqueConstraint=(fields['coach'],condition=models.Q(majorName__majorName='تکواندو'),name='unique_majorName__majorName_تکواندو')
        #constraints = [models.CheckConstraint(check=Q(coach=Coach.objects.filter(majors='تکواندو')), name='period_coach_تکواندو')]
       # constraints = [models.CheckConstraint(check=Q(coach__majors__majorName = models.F('major_majorName')) , name='period_coach_major')]
 
      #  constraints=[models.CheckConstraint(check=models.Q(salon__period_salonSet__gte='ژیمناستیک'),name="coach__majorName=majorName")]
        
 
# class Session(models.Model):
#     sessionID=models.IntegerField(primary_key=True,verbose_name='کد جلسه')
#     sessionName=models.CharField(max_length=20,verbose_name='نام جلسه')
#     Type=[('Normal','عادی'),('reparative','جبرانی'),('Extraordinary','فوق العاده'),('test','امتحان'),('Public holiday','تعطیل رسمی'),('Special holiday','تعطیل خاص')]
#     period=models.ForeignKey(Period,on_delete=models.CASCADE,verbose_name='دوره' )
#     TypeOfSession=models.CharField(max_length=100,choices=Type,verbose_name='نوع جلسه')
#     sessionDate=models.DateField(verbose_name='تاریخ')
#     started_at=models.TimeField(verbose_name='شروع')
#     ended_at=models.TimeField(verbose_name='پایان')
    
    
#     def __str__(self) -> str:
#         return self.sessionName   
    
#     class Meta:
#         verbose_name=' جلسه'
#         verbose_name_plural= 'جلسه ها'
#         db_table='T_Session'
  
# class AttendanceCoach(models.Model):
#     period=models.ForeignKey(Period,on_delete=models.CASCADE,verbose_name='نام دوره',null=True )
#     session=models.ForeignKey(Session,on_delete=models.CASCADE,verbose_name='جلسه' )
#     Date=models.DateField(verbose_name='تاریخ')
#     coach=models.ForeignKey(Coach,on_delete=models.CASCADE,verbose_name='نام استاد' )
#     situation=[('Present','حاضر'),('Delayed attendance','حضور با تاخیر'),('absence','عدم حضور')]
#     AttendanceStatus=models.CharField(max_length=100,choices=situation,verbose_name='وضعیت حضور')
    
#     def __str__(self) -> str:
#         return str(self.session)+'\t'+str(self.Date)+'\t'+str(self.coach)
    
#     class Meta:
#         verbose_name=' حضوروغیاب استاد'
#         verbose_name_plural= 'حضوروغیاب استادها'
#         db_table='T_AttendanceCoach'
       
# class AttendanceAthlet(models.Model):
#     period=models.ForeignKey(Period,on_delete=models.CASCADE, verbose_name='نام دوره',null=True)
#     session=models.ForeignKey(Session,on_delete=models.CASCADE,verbose_name='جلسه' )
#     Date=models.DateField(verbose_name='تاریخ')
#     Athlet=models.ForeignKey(athlete,on_delete=models.CASCADE ,verbose_name='ورزشکار')
#     situation=[('Present','حاضر'),('Delayed attendance','حضور با تاخیر'),('absence','عدم حضور')]
#     AttendanceStatus=models.CharField(max_length=100,choices=situation,verbose_name='وضعیت حضور')
    
#     def __str__(self) -> str:
#         return str(self.session)+'\t'+str(self.Date)+'\t'+str(self.Athlet)
#     class Meta:
#         verbose_name=' حضوروغیاب ورزشکار'
#         verbose_name_plural= 'حضوروغیاب ورزشکارها'
#         db_table='T_AttendanceAthlet'
        
# class Register(models.Model):
    
#     period=models.ForeignKey(Period,on_delete=models.CASCADE,blank=True,null=True )
#     athlete=models.ForeignKey(athlete,on_delete=models.CASCADE,blank=True,null=True)
#     PaySalary=models.IntegerField(default=0,verbose_name='پرداخت هزینه')
#     RegistrationDate=models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ثبت نام')
    
#     class Meta:
#         verbose_name='ورزشکار ثبت نام شده'
#         verbose_name_plural= 'ورزشکار های ثبت نام شده'
#         db_table='T_Register'
#         unique_together=(('period','athlete'),)
#     # SalaryStatus=models.IntegerField()
#     def __str__(self) -> str:
#         return  str(self.period) 
 
#     def salary(self):
#         return self.period.salary
#     def calculate_salary(self): 
#         # state =Period.objects.filter(salary=self.period.salary) 
       
#         pass 
   
 
    
#     def calc(self):
#         # item=iter(self.calculate_salary())
#         # for i in item:
#             return  1
#     #    return Register.objects.annotate(sum(iter(self.SalaryStatus)))
    
#     calc=property(calc)
#     SalaryStatus=property(calculate_salary )
 
#     SalaryStatus.fget.short_description='وضعیت شهریه'