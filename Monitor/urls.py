from django.urls import include, re_path
from Monitor import views

urlpatterns=[
    re_path(r'^user/$', views.userAPI)
]