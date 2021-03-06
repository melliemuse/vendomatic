import sqlite3
from django.shortcuts import render
from vendomaticapp.models import Beverage, Transaction
from .connection import Connection

def inventory_list(request):
    if request.method == 'GET':
        beverage = Beverage.objects.all()
        transaction = Transaction.objects.all()


        template = 'inventory.html'
        context = {
            'beverage': beverage,
            'transaction': transaction
        }
        print(request)

        return render(request, template, context)