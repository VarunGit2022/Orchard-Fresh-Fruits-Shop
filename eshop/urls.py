"""eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('fruit/',views.fruit,name='fruit'),
    path('contact/',views.contact,name='contact'),
    path('testimonial',views.testimonial,name='testimonial'),
    path('login/',views.user_login,name='login'),
    path('signup/',views.user_signup,name='signup'),
    path('logout/',views.user_logout,name='logout'),
    path('detail<int:id>/',views.detail,name='detail'),
    path('add_cart/',views.add_cart,name='add_cart'),
    # path('showcart/',views.move_to_cart,name='add_cart'),
    path('showcart/',views.show_cart,name='showcart'),
    # path('saveditems/',views.save_for_later,name='saveditems'),
    path('emptycart/',views.show_cart,name='emptycart'),
    path('pluscart/',views.plus_cart,name='pluscart'),
    path('minuscart/',views.minus_cart,name='minuscart'),
    path('removecart/',views.remove_cart,name='removecart'),
    path('checkout/',views.checkout,name='checkout'),
    path('address/',views.address,name='address'),
    path('profile/',views.profile,name='profile'),
    # path('profile1/',views.real_profile,name='profile1'),
    # path('booking/',views.booking,name='booking'),
    path('viewbooking/', views.view_booking, name='viewbooking'),
    path('search/',views.search,name='search'),


]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
