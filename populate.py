import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","lunch_box.settings")

import django
django.setup()

from reservation.models import OrderMenu,Order,ReservationData,Menu
from random import randint
from django.forms import formset_factory


def main():

    menu_name = ['Organic tomato salad, gorgonzola cheese, capers','Flatbread, feta cheese, cranberries, pinenuts','Baked broccoli','Grilled octopus salad, citrus emulsion'
    #              ,'Eggplant parmigiana','Natural angus beef burger with fries','Spicy meatballs','Handmade Gnocchi with black truffle cream','Sea salt and pepper calamari']
    # menu_list = [Menu.objects.create(name=item, stock=randint(5,10), price=randint(100,300)) for item in menu_name]
    # for item in menu_list:
    #     item.save()

    # menu_list = Menu.objects.all()
    # reservation = ReservationData.objects.all()[0]
    # quantity = 1
    #
    # for i in range(6):
    #     new_order = OrderMenu.objects.create(menu_name=menu_list[randint(0,len(menu_list))],quantity=quantity,reservation=reservation)
    #     new_order.save()

    # print("Order created")
    pass

main()
