from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import ListView
from .models import ReservationData,OrderMenu
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect


#List all reservations
class ReservationListView(ListView):
    login_url = reverse_lazy('auth_login')
    model = ReservationData
    template_name = 'reservation/reservation_list.html'
    context_object_name = 'reservations'

    def get(self, request, *args, **kwargs):
        print(request.user.is_authenticated)
        if not request.user.is_authenticated:
            return redirect(self.login_url)
        else :
            response = super(ReservationListView, self).get(request=request,kwargs=kwargs)
            return response

    def get_queryset(self):
        username = self.request.user
        return ReservationData.objects.filter(reserved_by=username)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reservation_edit_form'] = ReservationUpdate(request=self.request).get_form()
        return context

#Create a reservation
class ReservationCreate(CreateView):
    model = ReservationData
    fields = ['seat','reserved_time']
    template_name = 'reservation/reservation_create.html'

    def form_valid(self, form):
        new_reservation = form.save(commit=False)
        print(new_reservation.reserved_time.date()," : ",new_reservation.reserved_time.time())
        new_reservation.reserved_by = self.request.user
        new_reservation.save()
        self.request.session['reservation_id'] = new_reservation.id
        return redirect(reverse_lazy('reservation:order-list'))

#Delete a reservation
class ReservationDelete(DeleteView):
    model = ReservationData
    success_url = reverse_lazy('reservation:list')

#Update a reservation
class ReservationUpdate(UpdateView):
    model = ReservationData
    fields = ['seat','reserved_time']
    success_url = reverse_lazy('reservation:list')

#List all orders
class OrderListView(ListView):
    model = OrderMenu
    context_object_name = 'orders'
    template_name = 'reservation/order_list.html'
    
    def get_context_data(self, **kwargs):
        context = OrderMenu.objects.filter(reservation=ReservationData.objects.get(id=self.request.session['reservation_id']))
        context = {'orders':context}
        total_cost = sum([order.get_cost() for order in context['orders']])
        total_quantity = sum([order.quantity for order in context['orders']])
        context['total_quantity'] = total_quantity
        context['total_cost'] = total_cost
        context['order_create_form'] = OrderCreate(request=self.request).get_form()
        context['order_edit_form'] = OrderUpdate(request=self.request).get_form()
        return context

#Create a new order
class OrderCreate(CreateView):
    model = OrderMenu
    context_object_name = 'form'
    fields = ['quantity','menu_name']
    success_url = reverse_lazy('reservation:order-list')

    def get_context_data(self, **kwargs):
        context = super(OrderCreate, self).get_context_data(**kwargs)
        context['reservation_id'] = self.request.session['reservation_id']
        return context

    def form_valid(self, form):
        new_order = form.save(commit=False)
        print("Reservation id : ")
        new_order.reservation = ReservationData.objects.get(id=self.request.session['reservation_id'])
        new_order.save()
        return redirect(self.success_url)

#Update an order
class OrderUpdate(UpdateView):
    model = OrderMenu
    fields = ['quantity','menu_name']
    success_url = reverse_lazy('reservation:order-list')

#Delete an order
class OrderDelete(DeleteView):
    model = OrderMenu
    success_url = reverse_lazy('reservation:order-list')
