from django.contrib import admin
from models import FacebookFanpage, ExtendedUser, FacebookPost


class ExtendedUserAdmin(admin.ModelAdmin):
    readonly_fields = ('facebook_id', 'access_token', 'app_id', 'date_joined', 'last_login', 'raw_facebook_profile')
    list_filter = ('date_joined', 'last_login', 'is_staff', 'is_active', 'app_id')
    list_display = ( 'facebook_id', 'app_id', 'date_joined', 'last_login', 'is_active')


class FacebookFanpageAdmin(admin.ModelAdmin):
    list_display = ('fanpage_url', 'is_valid')

class FacebookPostAdmin(admin.ModelAdmin):
    list_display = ('id','user','post_id','is_deleted','is_finished','created_at','modified_at','delete_after','error_delete')
    list_filter = ('created_at','is_deleted','is_finished','delete_after')

admin.site.register(FacebookFanpage, FacebookFanpageAdmin)
admin.site.register(ExtendedUser, ExtendedUserAdmin)
admin.site.register(FacebookPost,FacebookPostAdmin)