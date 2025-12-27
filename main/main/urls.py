from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('product/', include('product.urls')),
    path('api/', include('orders.urls')),
    path('api/', include('Business.urls')),
    path('api/', include('service_section.Serviceproduct.urls')),
    path('api/', include('service_section.Payment.urls')),
    path('api/', include('service_section.Subject.urls')),
    path('api/', include('service_section.Serviceorder.urls')),
]
