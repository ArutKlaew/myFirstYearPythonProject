from django.conf.urls import url,include
from django.contrib import admin
from home.views import HomeView

urlpatterns = [
    url(r'^$',HomeView.as_view(),name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^home/',include('home.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^reservation/',include('reservation.urls')),
]
