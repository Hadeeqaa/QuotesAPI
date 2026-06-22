from django.urls import path,include
from . import views

urlpatterns = [
    path('register/',views.UserView.as_view(),name='registser'),
    path('quotes/',views.QuotesView.as_view(),name='QuotesView'),
    path('logout/', views.custom_logout_view, name='logout')
]