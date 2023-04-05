from django.contrib import admin
from django.urls import path
from firstapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('about/',views.about),
    path('service/',views.service),
    path('gallery/',views.gallery),
    path('reservation/',views.reservation),
    path('contact/',views.contact),
    path('login/',views.login),
    path('order/',views.order),
    path('payment/',views.payment),
    path('bill/',views.bill),
    path('info/',views.info),
    path('signup/',views.signup),
    path('logout/',views.logout)
]