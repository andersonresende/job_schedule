from django.contrib import admin
from .models import Service, Employee, CategoryEmployee, CategoryService


admin.site.register(
    [
        Service,
        Employee,
        CategoryEmployee,
        CategoryService
    ]
)

