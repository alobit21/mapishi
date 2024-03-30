from .import views
from django.urls import path

from .views import upload_image, show_images
urlpatterns = [
 path('', views.home, name='home'),
 path('register/', views.register, name='register'),
path('login/', views.login, name='login'),
path('products/', views.products, name='products'),

path('buy/', views.buy, name='buy'),
path('order/', views.order, name="order"),
path('upload_image/', views.upload_image, name='upload_image'),
path('show_images/', views.show_images, name='show_images'),

]



