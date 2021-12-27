from django.urls import path
from . import views

urlspatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls"),
]