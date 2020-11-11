
from django.urls import path
from . import views
urlpatterns = (
    path('', views.homepage , name='home'),

    path('login/' , views.loginPage , name='loginPage'),
    path('logout/' , views.logoutPage , name='logoutPage'),

  
    path('product/<str:pk>/' , views.product , name='product'),
    path('callback/' , views.callBack , name='callBack'),
    path('policy/' , views.policy , name='policy'),
    path('about/' , views.about , name='about'),
    path('protfolio-returns/', views.port , name='port'),
    path('certi/' , views.certi , name='certi'),
    
)