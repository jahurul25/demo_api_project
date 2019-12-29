from django.contrib import admin
from . import models
# Register your models here.


class UserListAdmin(admin.ModelAdmin):
    list_display = ['user_name','user_type','user_full_name','user_email','status']
    search_fields  = ['user_name','user_email','user_mobile']
    list_filter  = ['user_type','status']

class InspectionInfoAdmin(admin.ModelAdmin):
    list_display = ['serial_number','distributor_name','user_name','action_taken','status']
    search_fields  = ['serial_number','distributor_name']
    list_filter  = ['status']

class DistributorInfoAdmin(admin.ModelAdmin):
    list_display = ['distributor_name','distributor_type','address','status']
    search_fields  = ['distributor_name','distributor_type']
    list_filter  = ['status']

admin.site.register(models.UserInfo, UserListAdmin)
admin.site.register(models.InspectionInfo, InspectionInfoAdmin)
admin.site.register(models.DistributorInfo, DistributorInfoAdmin)