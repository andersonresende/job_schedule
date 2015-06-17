from django.contrib import admin
from .models import (
    Service,
    Employee,
    CategoryEmployee,
    DefaultCategoryService,
    CustomCategoryService
)


class ServiceAdmin(admin.ModelAdmin):
    model = Service


admin.site.register(Service, ServiceAdmin)
admin.site.register(
    [
        Employee,
        CategoryEmployee,
        DefaultCategoryService,
        CustomCategoryService,
    ]
)

