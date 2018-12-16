from django.contrib import admin
from .models import *

class usertopic_inline(admin.TabularInline):
    model = UserTopic
    extra = 0

class ProfileAdmin(admin.ModelAdmin):
    inlines = (usertopic_inline,)

class UserTopicAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False

admin.site.register(Profile, ProfileAdmin)
admin.site.register(UserTopic, UserTopicAdmin)