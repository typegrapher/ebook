from django.urls import path
from . import views
from django.views.static import serve


app_name='web'

urlpatterns = [
    path('', views.index,name='index'),
    path('login', views.login_view,name='login'),
    path('signup/', views.signup, name='signup_view'),
    path('logout', views.logout_view, name='logout'),
    path('about', views.about,name='about'),
    path('contact', views.contact,name='contact'),
    path('shop', views.shop,name='shop'),
    path('single_page/<int:id>/', views.single_page, name='single_page'),
]