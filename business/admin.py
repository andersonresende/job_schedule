from django.contrib import admin
from django.contrib.admin import AdminSite
from django import forms
from django.contrib.admin.templatetags.admin_urls import add_preserved_filters
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

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
    class Media:
        css = {
            "all": ("schedule/css/business_admin.css",)
        }

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
        'default_category_service',
        'reference',
        'urgency_status',
        'closed'
    ]
    list_filter = ['closed']
    filter_horizontal = ['employees']

    def response_post_save_change(self, request, obj):
        """
        Figure out where to redirect after the 'Save' button has been pressed
        when editing an existing object.
        """
        post_url = reverse("month_calendar", kwargs={'calendar_slug': 'default'})
        return redirect(post_url)

    def response_post_save_add(self, request, obj):
        """
        Figure out where to redirect after the 'Save' button has been pressed
        when adding a new object.
        """
        post_url = reverse("month_calendar", kwargs={'calendar_slug': 'default'})
        return redirect(post_url)


class BasicAdminSite(AdminSite):
    site_header = 'Job Schedule'
    index_template = 'index.html'
    app_index_template = 'app_index.html'


admin_site = BasicAdminSite(name='basic_admin_site')
admin_site.register(User, UserAdmin)
admin_site.register(Service, ServiceAdmin)
admin_site.register(
    [
        Employee,
        CategoryEmployee,
        DefaultCategoryService,
        CustomCategoryService,
        Holiday,
    ]
)
