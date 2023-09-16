"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from category.views import CategoryListCreateDetailView, CategoryDetailView
from products.views import ProductListCreateRetrieveView, ProductDetail
from authentication.views import MyTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),  # Include DJOSER URLs
    path('auth/', include('djoser.urls.authtoken')),
    path('api/', include('rest_framework.urls')),
    path('categories/', CategoryListCreateDetailView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-retrieve-update-delete'),
    path('products/', ProductListCreateRetrieveView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-retrieve'),
    path("auth/jwt/create/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
