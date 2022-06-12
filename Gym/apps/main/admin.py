 
 
 
 
from django.contrib import admin

# Register your models here.
from django.db.models import F

# Register your models here.
from django.http import HttpResponseRedirect
from .models import *
from .models import Major
from django.urls import path
from django.utils.html import format_html
from ..main.validation import validate_Capacity
from django.core.exceptions import ValidationError
from django.db.models import Q

# Register your models here.
 
@admin.register(salon)
class salonAdmin(admin.ModelAdmin):
    list_display=('SalonName','Capacity','Is_Active','click_me')
    list_filter=('Capacity','Is_Active')
    search_fields=('SalonName','Capacity','Is_Active' )
    change_list_template='admin/salons/salons_change_list.html'
  
    def get_urls(self):
        urls=super().get_urls()
        custome_urls=[
            path('Capacityvalue/<int:value>/',self.change_Capacity_value)
        ]
        return custome_urls+urls
    
    
    def change_Capacity_value(self,request,value):
        try:
            val= validate_Capacity(value)
            self.model.objects.all().update(Capacity=val)
            self.message_user(request,'مقدار ظرفیت با موفقیت تغییر کرد')
            return HttpResponseRedirect("../")
        except  ValidationError as error:
            self.message_user(request,error,level="error")
            return HttpResponseRedirect("../")
            
    def click_me(self,obj):
        return format_html(f'<a href="/admin/main/salon/{obj.id}/change/" class="default" style="color:rgb(26, 119, 159)">View</a>')
    click_me.short_description=' ویرایش '
    
#-------------------------------------------------------------------------------------------------------------
  
@admin.register(Major)
class majorAdmin(admin.ModelAdmin):
    list_display=('majorName','MajorGroup','is_active','click_me')
    list_filter=( 'is_active','MajorGroup')
    search_fields=('MajorGroup','is_active')
    list_per_page=2
    def click_me(self,obj):
        return format_html(f'<a href="/admin/main/major/{obj.id}/change/" class="default" style="color:rgb(26, 119, 159)">View</a>')
    click_me.short_description=' ویرایش ' 
#-----------------------------------------------------------------------------------------------------------------    
 
@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    list_display=('GymName','click_me')
    search_fields=('GymName', ) 
    
    def click_me(self,obj):
        return format_html(f'<a href="/admin/main/Gym/{obj.id}/change/" class="default" style="color:rgb(26, 119, 159)">View</a>')
    
    click_me.short_description=' ویرایش '
#---------------------------------------------------------------------------------------------------------------------------
@admin.register(TypePriod)
class TypePriodAdmin(admin.ModelAdmin):
    list_display=('id','title','click_me')
    
    def click_me(self,obj):
        return format_html(f'<a href="/admin/main/typepriod/{obj.id}/change/" class="default" style="color:rgb(26, 119, 159)">View</a>')
    
    click_me.short_description=' ویرایش '
#-------------------------------------------------------------------------------------------------------------------------- 
from .form import PeriodForm
@admin.register(Period)
class periodAdmin(admin.ModelAdmin):
    list_display=('periodName','salon','major','typeOfPeriod', 'salary','Capacity','startDate_at','timestarted_at','timeended_at' ,'get_major',
                  'click_me')
    list_filter=('Capacity','timestarted_at','timeended_at')
    search_fields=('majorName','salon')
   
 
 
    def _get_Period_major(self,obj):
        try:
           return obj
        except:
            pass
     
    def  majorName(self,obj):
    
       majors=obj.objects.get(name__iexact=obj.major)
    #    for item in majors:
    #        print(item.majorName)
       print('majors',majors)
       return majors
 
    # _get_Period_major.short_description='تخصص'
    
    my_id_for_formfield = None
    
    # def get_form(self, request, obj=None, **kwargs):
    #     if obj:
    #         self.my_id_for_formfield = obj.major
    #     return super(periodAdmin, self).get_form(request, obj, **kwargs)
  
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "coach"  :
             
            # object=self.model.objects.filter(major__majorName__in='تکواندو')
            # print(object)
            # object=[item.majorName for item in self.model.objects.select_related('major')]
            # print(object)
            # f=self.model.objects.get(major__majorName=filter=) 
            # print(f)
            # majors= self.get_object(request,self.model.get_major)
            # majors=request.resolver_match.kwargs[self.model.get_major]
            kwargs["queryset"] =Coach.objects.filter(majorName__majorName= 'کاراته')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    
    
    def click_me(self,obj):
        return format_html(f'<a href="/admin/main/period/{obj.id}/change/" class="default" style="color:rgb(26, 119, 159)">View</a>')
    
    click_me.short_description=' ویرایش '
    
# #------------------------------------------------------------------------------------------------------------------------------
@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display=('CoachName','CoachFamily','phone_number','get_majors','click_me')
    def get_majors(self, obj):
        return "\n".join([m.majorName for m in obj.majorName.all()])
    get_majors.short_description='تخصص'
    
    def click_me(self,obj):
        return format_html(f'<a href="/admin/main/coach/{obj.id}/change/" class="default" style="color:rgb(26, 119, 159)">View</a>')
    
    click_me.short_description=' ویرایش '
# #------------------------------------------------------------------------------------------------------------------------------
@admin.register(majorGroups)
class majorGroupsAdmin(admin.ModelAdmin):
    list_display=('id','title' )
    list_filter=('title' , )
    search_fields=('title', )
 
 
# #---------------------------------------------------------------------------------------------------------------------------
# @admin.register(Session)
# class SessionAdmin(admin.ModelAdmin):
#     list_display=('sessionID','sessionName','TypeOfSession','period','sessionDate','started_at','ended_at')
#     list_filter=('period','sessionDate','started_at')
#     search_fields=('period','sessionDate')
# #---------------------------------------------------------------------------------------------------------------------------- 
# @admin.register(AttendanceCoach) 
# class AttendanceCoachAdmin(admin.ModelAdmin):
#     list_display=('coach','period','session','Date','AttendanceStatus' )
#     list_filter=('session','Date','AttendanceStatus')
#     search_fields=('Date','session')
        
# #--------------------------------------------------------------------------------------------------------------------------- 
# @admin.register(AttendanceAthlet)
# class AttendanceAthletAdmin(admin.ModelAdmin):
#     list_display=('Athlet','period','session','Date','AttendanceStatus' )
#     list_filter=('session','Date','AttendanceStatus')
#     search_fields=('Date','session')
# #-------------------------------------------------------------------------------------------------------------------------------
# @admin.register(Register) 
# class RegisterAdmin(admin.ModelAdmin):
#     list_display=('period','athlete','PaySalary','RegistrationDate','SalaryStatus','calc')
#     list_filter=('period',)
    