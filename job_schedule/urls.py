from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from business.admin import admin_site
from business.views import CalcFinalDateView, CheckEmployeesServicesView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'job_schedule.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^basic-admin/', include(admin_site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^schedule/', include('schedule.urls')),
    url(r'^calc-final-date/$', CalcFinalDateView.as_view(), name='calc-final-date'),
    url(r'^check-employees-services/$', CheckEmployeesServicesView.as_view(), name='check-employees-services'),

)

# Serving static files in development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serving media files in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

