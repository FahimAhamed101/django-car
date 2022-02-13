from django.contrib import admin

# Register your models here.
from .models import Contacts

class ContactAdmin(admin.ModelAdmin):
    

    
    list_display=('id','first_name','last_name','car_title','email','city','created_date')
    list_display_links=('id','first_name','last_name',)
    search_field=('frist_name','last_name','car_title','email',)
    List_filter=('designation','body_style','fuel_type','is_featured','description')
    list_per_page=25

admin.site.register(Contacts,ContactAdmin)