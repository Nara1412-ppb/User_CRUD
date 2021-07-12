from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
# Register your models here.
User = get_user_model()

class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with no username field."""
    fieldsets = (
        (None, {'fields': ('FirstName', 'LastName','EmailId', 'password')}),
        ('Personal info', {'fields': ('MobileNo','DOB','Address','Gender','CountryName','CityName','Skills')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('FirstName', 'LastName','EmailId','MobileNo', 'password1', 'password2'),
        }),
    )
    list_display = ('FirstName', 'LastName','EmailId','is_staff','MobileNo')
    search_fields = ('FirstName','EmailId','MobileNo')
    ordering = ('EmailId',)

admin.site.register(User,CustomUserAdmin)