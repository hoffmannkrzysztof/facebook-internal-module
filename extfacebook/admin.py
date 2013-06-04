from django.contrib import admin
from models import FacebookFanpage, ExtendedUser


class ExtendedUserAdmin(admin.ModelAdmin):
    readonly_fields = ('facebook_id', 'access_token', 'app_id', 'date_joined', 'last_login', 'raw_facebook_profile')
    list_filter = ('date_joined', 'last_login', 'is_staff', 'is_active', 'app_id')
    list_display = ( 'facebook_id', 'app_id', 'date_joined', 'last_login', 'is_active')


class FacebookFanpageAdmin(admin.ModelAdmin):
    list_display = ('fanpage_url', 'is_valid')


admin.site.register(FacebookFanpage, FacebookFanpageAdmin)
admin.site.register(ExtendedUser, ExtendedUserAdmin)