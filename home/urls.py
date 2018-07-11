from django.conf.urls import url
from home import views

app_name = 'home'

urlpatterns = [
    url(r'^$',views.HomeView.as_view(),name='index'),
]
