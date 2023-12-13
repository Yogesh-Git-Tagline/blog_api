import blog_api
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog_api/', include('blog_api.urls')),
    path('auth/', include('rest_framework.urls'))
]
