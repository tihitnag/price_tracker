from django.urls import path
from . import views
urlpatterns = [
    path('',views.ProductListView.as_view(),  name="product-list"),
    path('add',views.ProductAddView.as_view(),  name="add-product"),
    path('<int:pk>/delete/', views.ProductDeleteView.as_view(), name='delete-product'),
    
]