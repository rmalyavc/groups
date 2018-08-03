from django.contrib import admin
from .models import Group, Elem

class GroupAdmin(admin.ModelAdmin):
	list_display = ['name', 'description']
	list_filter = ['name']

class ElemAdmin(admin.ModelAdmin):
	list_display = ['name', 'description']
	list_filter = ['name']

admin.site.register(Group, GroupAdmin)
admin.site.register(Elem, ElemAdmin)