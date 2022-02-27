from django.urls import path
from orders import views

urlpatterns = [

    path('', views.OrderCreateListView.as_view(), name='order_list'),
    path('<str:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('update-status/<str:pk>/',
         views.UpdateOrderStatus.as_view(), name='order_update'),
    path('user/<str:user_id>/orders/',
         views.UserOrdersView.as_view(), name='user_orders'),
    path('user/<str:user_id>/orders/<str:pk>/',
         views.UserOrderDetailView.as_view(), name='user_order_detail'),
]
