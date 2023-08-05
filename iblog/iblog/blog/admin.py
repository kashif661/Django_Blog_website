from django.contrib import admin
from .models import Category,Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','description','url','add_date')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post)

# Register your models here.
