from django.contrib import admin
from django.urls import path, include
from users.urls import urlpatterns as user_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(user_urls)),
]
