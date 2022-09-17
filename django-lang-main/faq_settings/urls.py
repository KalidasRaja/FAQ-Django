from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('faq-detail/', views.faq_view.as_view(), name='faq_view')

]
