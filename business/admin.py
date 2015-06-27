from django.contrib import admin
from django import forms

from .models import (
    Service,
    Employee,
    CategoryEmployee,
    DefaultCategoryService,
    CustomCategoryService,
    Holiday,
)


class ServiceForm(forms.ModelForm):
    model = Service

    reference = forms.CharField(max_length=10)

    def clean(self):
        cleaned_data = super(ServiceForm, self).clean()
        default_category_service = cleaned_data.get("default_category_service")
        custom_category_service = cleaned_data.get("custom_category_service")

        if not default_category_service and not custom_category_service:
            self.add_error('default_category_service', "Select one category service.")
            raise forms.ValidationError("Please, choose at least one Category Service.")


class ServiceAdmin(admin.ModelAdmin):
    model = Service
    form = ServiceForm
    exclude = [
        'creator',
        'rule',
        'end_recurring_period',
        'calendar'
    ]
    list_display = [
        'title',
        'reference',
        'urgency_status'
    ]


admin.site.register(Service, ServiceAdmin)
admin.site.register(
    [
        Employee,
        CategoryEmployee,
        DefaultCategoryService,
        CustomCategoryService,
        Holiday,
    ]
)

