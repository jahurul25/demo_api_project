from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Demo Project Super Admin Panel"
admin.site.site_title = "Demo Project Super Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('testapp.urls')),
]
