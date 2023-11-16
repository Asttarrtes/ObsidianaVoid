from django.contrib import admin
from django.urls import path
from index.views import index
from control.views import control
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index , name="index"),
    path("control/", control , name="control")
]
