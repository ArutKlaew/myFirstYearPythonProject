from django.conf.urls import url
from reservation import views
from django.contrib.auth.decorators import login_required

app_name = 'reservation'

urlpatterns = [
    url(r'^$', login_required(views.ReservationListView.as_view()), name='list'),
    url(r'^create/$', login_required(views.ReservationCreate.as_view()), name='create'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(views.ReservationUpdate.as_view()), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(views.ReservationDelete.as_view()), name='delete'),
    url(r'^order/list/$', login_required(views.OrderListView.as_view()), name='order-list'),
    url(r'^order/create/$', login_required(views.OrderCreate.as_view()), name='order-create'),
    url(r'^order/edit/(?P<pk>\d+)/$', login_required(views.OrderUpdate.as_view()), name='order-update'),
    url(r'^order/delete/(?P<pk>\d+)/$', login_required(views.OrderDelete.as_view()), name='order-delete'),
]
