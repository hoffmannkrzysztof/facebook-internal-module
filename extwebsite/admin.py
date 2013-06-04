from django.contrib import admin
from models import Website


class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'domain', 'app_id', 'is_valid')


admin.site.register(Website, WebsiteAdmin)