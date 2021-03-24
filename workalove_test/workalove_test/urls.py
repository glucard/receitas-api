from django.contrib import admin
from django.urls import path, include

from receitas.urls import receitas_urls

api_urls = [
    path('', include(receitas_urls)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
]
