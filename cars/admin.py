from django.contrib import admin
from .models import Cars
from django.utils.html import format_html

class CarAdmin(admin.ModelAdmin):
    def thumbnail(Self,object):
        return format_html('<img src="{}" width="40" style="border-radius:50px; "/>'.format(object.car_photo.url))

    thumbnail.shortdescription = 'car_photos'
    list_display=('id','thumbnail','car_title','city','color','model','year','body_style','fuel_type','is_featured','description','created_date')
    list_display_links=('id','thumbnail','car_title',)
    list_editable=('is_featured',)
    search_field=('id','car_title','city','color','model')
    List_filter=('designation','body_style','fuel_type','is_featured','description')


admin.site.register(Cars,CarAdmin)