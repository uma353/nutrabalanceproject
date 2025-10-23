"""
URL configuration for nutrabalance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from main import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'product', views.ProductViewSet, basename='product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('benifits/', views.benifits, name='benifits'),
    path('ingredient/', views.ingredient, name='ingredient'),
    path('ereview/', views.ereview, name='ereview'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),

    path('view1/', views.view1, name='view1'),
    path('view2/', views.view2, name='view2'),
    path('view3/', views.view3, name='view3'),
    path('view4/', views.view4, name='view4'),
    path('view5/', views.view5, name='view5'),
    path('view6/', views.view6, name='view6'),
    path('view7/', views.view7, name='view7'),
    path('view8/', views.view8, name='view8'),
    path('view9/', views.view9, name='view9'),
    path('view10/', views.view10, name='view10'),
    path('view11/', views.view11, name='view11'),
    path('view12/', views.view12, name='view12'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('logout/', views.logout_view, name='logout'),
    path('register/', views.signup_view),
    path('api/', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('data/', views.dataview),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)