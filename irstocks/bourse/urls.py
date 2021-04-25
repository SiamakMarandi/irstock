from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('filter/', views.filter, name="filter"),
    path('test/', views.test, name="test"),
    path('alaki/', views.alaki, name="alaki"),
    path('shares_info/', views.shares_info, name="shares"),
    path('database_filler', views.database_filler, name="filler"),
    path('prepared_filter', views.prepared_filter, name="prepared_filter"),
    path('signup', views.signup, name="signup"),

]
