from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.views.generic import RedirectView
from business.admin import admin_site
from business.views import CalcFinalDateView, CheckEmployeesServicesView
from schedule.periods import Month

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/basic-admin')),
    url(r'^basic-admin/', include(admin_site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^calendar/month/(?P<calendar_slug>[-\w]+)/$',
        'schedule.views.calendar_by_periods',
        name="month_calendar",
        kwargs={'periods': [Month], 'template_name': 'schedule/calendar_month.html'}),
    url(r'^calc-final-date/$', CalcFinalDateView.as_view(), name='calc-final-date'),
    url(r'^check-employees-services/$', CheckEmployeesServicesView.as_view(), name='check-employees-services'),

)

# Serving static files in development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serving media files in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

