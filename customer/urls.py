from django.urls import path
from customer import views 
 
app_name = 'customer'

urlpatterns = [ 
    path('customer/customers/', views.customer_list) ,
    path('customer/customers/<int:pk>/', views.customer_detail),
]