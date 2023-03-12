from django.contrib import admin
from .models import AppUser
# Register your models here.
@admin.register(AppUser)
class UserAdmin(admin.ModelAdmin):
    list_display=('user', 'userType', 'showGender','city', 'zipcode')

    def userType(self, obj):
        return obj.get_user_type_display()
    userType.short_description='User Type'

    def showGender(self, obj):
        return obj.get_gender_display()
    showGender.short_description='Gender'