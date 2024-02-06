"""
URL configuration for Estore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Estore import settings
from Store.views import GunsAPIView, GunDetailView, OrderListView, OrderRetrieveView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Store.urls')),
    path('api/drf-auth', include('rest_framework.urls')),
    path('api/gunlist', GunsAPIView.as_view(), name='gunlist'),
    path('api/gun/<int:pk>/', GunDetailView.as_view(), name='gun-detail'),
    path('api/orders/',OrderListView.as_view(), name='order-list'),
    path('api/order/<int:pk>',OrderRetrieveView.as_view(), name='order-detail') ,
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
