from django.contrib import admin
from .models import Company, Machine, Specs
from django.utils.html import format_html


class StackedSpecsAdmin(admin.TabularInline):
    model = Specs
    fields = ("label", "value", "machine")
    readonly_fields = ("machine",)
    extra = 1

    def has_add_permission(self, request, *args, **kwargs):
        return True


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ("name", "company_website", "company", "is_active", "description")

    list_filter = ("is_active",)

    search_fields = ("name__icontains",)

    readonly_fields = ("created", "modified")

    inlines = (StackedSpecsAdmin,)

    def company_website(self, obj):
        return format_html(f'<a href="{obj.company.website}">company Website</a>')


class StackedMachinesAdmin(admin.TabularInline):
    model = Machine
    fields = ("name", "is_active", "created", "modified")
    readonly_fields = ("created", "modified")
    extra = 0

    def has_add_permission(self, request, *args, **kwargs):
        return False


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = (StackedMachinesAdmin,)
