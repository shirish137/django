from django.contrib import admin
from blogapp.models import Blog 
# Register your models here.
#admin.site.register(Blog)
#step1: Define ModelAdminClass
class BlogAdmin(admin.ModelAdmin):

    list_display=['id','title','detail','cat','is_published','created_at']
    list_filter=('cat','is_published')

#step2: Register model with ModelAdminClass i.e BlogAdmin 
admin.site.register(Blog,BlogAdmin)
