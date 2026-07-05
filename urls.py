from djaongo.contrib import admin
from django.urls import path, include

urlpatterns=[
    path('admin/',admin.site.urls),
    path('menu/', include('menu.urls')),
    path('orders/',include('orders.urls')),
    path('', include('menu.urls')),
]