from django.contrib import admin
from .models import ReservationData,Menu,OrderMenu

admin.site.register(ReservationData)
admin.site.register(Menu)
admin.site.register(OrderMenu)