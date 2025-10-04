from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('report/', views.report_item, name='report_item'),
    path('items/', views.item_list, name='item_list'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
]
