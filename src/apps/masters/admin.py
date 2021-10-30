from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import  MasterChangeForm, MasterCreationForm
from .models import Master


@admin.register(Master)
class MasterAdmin(UserAdmin):
    add_form = MasterCreationForm
    form = MasterChangeForm
    model = Master

    list_display = ('username', 'sex', 'age')
    list_filter = ('is_staff', 'is_active', 'sex')

    fieldsets = (
        (None, {'fields': ('username', 'password', 'sex', 'age')}),
        ('Permissions', {'fields': (
            'is_staff', 'is_active',
        )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'password1', 'password2',
                'sex', 'age', 'is_staff', 'is_active',
            ),
        }),
    )
    search_fields = (
        'username',
    )
    ordering = ()
    filter_horizontal = ()


admin.site.unregister(Group)