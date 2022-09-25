from cgitb import handler
from django.urls import path,include
from django.contrib import admin


admin.site.site_header = "VRL ADMINISTRATION PANEL"
admin.site.site_title = "VRL ADMIN PORTAL"
admin.site.index_title = "Welcome to VRL DATABASE Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
