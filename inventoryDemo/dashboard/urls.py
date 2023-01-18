from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.index,name='dashboard-index'),
    path('staff/', views.staff,name='dashboard-staff'),
    path('product/', views.product,name='dashboard-product'),
    path('order/', views.order,name='dashboard-order'),   
    path('product/delete/<int:pk>/', views.product_delete,name='dashboard-product-delete'),   
    path('product/update/<int:pk>/', views.product_update,name='dashboard-product-update'),
       
    path('staff/detail/<int:pk>/', views.staff_detail,name='dashboard-staff-detail'),   
    ]