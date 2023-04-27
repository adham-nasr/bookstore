from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns =[
    path('',views.home),
    path('loaddata/',views.load_data),
    path('mybooks/',login_required(views.MybooksView.as_view()))
]
