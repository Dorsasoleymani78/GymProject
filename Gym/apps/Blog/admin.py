from django.contrib import admin

# Register your models here.
from .models import Article, Category,settings
from django.utils.html import format_html
from django.utils.translation import ngettext
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatewords


@admin.action(description=' انتشار مقالات انتخاب شده')
def make_published(modeladmin, request, queryset):
    updated = queryset.update(status='Publish')
    modeladmin.message_user(request, ngettext(
            '%d مقاله انتشار شد.',
            '%d مقالات انتشار شدند.',
            updated,
    ) % updated, messages.SUCCESS)
    
    
@admin.action(description=' پیش نویس  مقالات انتخاب شده')
def make_Draf(modeladmin, request, queryset):
    updated = queryset.update(status='Draf')
    modeladmin.message_user(request, ngettext(
            '%d مقاله پیش نویس شد.',
            '%d مقالات پیش نویس شدند.',
            updated,
    ) % updated, messages.SUCCESS)
    
@admin.register(Article)
class BlogAdmin(admin.ModelAdmin):
    readonly_fields=('photo_tag',)
    list_display=('title','category_to_str','author','les_content','photo_tag','j_publish','j_update','status','is_active','click_me')
    list_filter=('is_active','create_at','author')
    search_fields=['category']
    prepopulated_fields={'slug':('title',)}
    ordering=['-status','-published_at']
    list_per_page=2
    actions = [make_published,make_Draf]
    
    def les_content(self,obj):
    #    return format_html(f'<p>{{obj.content|safe|truncatewords:30}}</p>')
        trun=truncatewords(obj.content,50)
        return  mark_safe(trun)
    les_content.short_description='متن مقاله'
    
    def click_me(self,obj):
        return format_html(f'<a href="/admin/Blog/article/{obj.id}/change/" class="default" style="color:rgb(26, 119, 159)">View</a>')
    click_me.short_description=' ویرایش '
        
    def photo_tag(self,obj):
        return format_html(f'<img  src="/media/{obj.img}" style=height:100px;width:100px;border-radius:5%;>')
    photo_tag.short_description='تصویر'
    




@admin.action(description=' فعال شدن دسته بندی انتخاب شده')
def make_active(modeladmin, request, queryset):
    updated = queryset.update(status='True')
    modeladmin.message_user(request, ngettext(
            '%d مقاله فعال شد.',
            '%d مقالات فعال شدند.',
            updated,
    ) % updated, messages.SUCCESS)
    
    
@admin.action(description=' غیر فعال شدن دسته بندی انتخاب شده')
def make_disactive(modeladmin, request, queryset):
    updated = queryset.update(status='False')
    modeladmin.message_user(request, ngettext(
            '%d مقاله غیر فعال شد.',
            '%d مقالات غیر فعال شدند.',
            updated,
    ) % updated, messages.SUCCESS)
    
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):    
    list_display=('id','title','parent','slug','status','position','click_me')
    list_filter=('status', )
    search_fields=('title','slug')
    prepopulated_fields={'slug':('title',)}
    actions = [make_active,make_disactive ]
    
    def click_me(self,obj):
        return format_html(f'<a href="/admin/Blog/category/{obj.id}/change/" class="default" style="color:rgb(26, 119, 159)">View</a>')
    click_me.short_description=' ویرایش '
    
@admin.register(settings)
class settingAdmin(admin.ModelAdmin):
    list_display=('title','click_me')
    search_fields=('title', )
    
    
    def click_me(self,obj):
        return format_html(f'<a href="/admin/Blog/settings/{obj.id}/change/" class="default" style="color:rgb(26, 119, 159)">View</a>')
    click_me.short_description=' ویرایش '
    