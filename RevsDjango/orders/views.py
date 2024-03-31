import json
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.db import connection

currentPrice = 0.0
currentOrder = []

class MenuItem:
    def __init__(self, description, price, id):
        self.description = description
        self.price = price
        self.id = id

# Initializes all the menu items buttons
def orders(request):
    with connection.cursor() as cursor:
        # Gets a list of all the menu items and sorts in alphabetical order
        cursor.execute("SELECT description, price, id FROM menu_items")
        data = cursor.fetchall()
        data.sort()
        buttonData = [{'description': currentItem[0], 'price': currentItem[1], 'id': currentItem[2]} 
                        for currentItem in data]

        context = {'buttonData': buttonData}
        return render(request, 'orders/orders.html', context)


# Adds menu item button functionality
def addItem(request):
    global currentPrice
    global currentOrder

    data = json.loads(request.body)
    description = data.get('description')
    price = data.get('price')
    id = data.get('id')
    currentPrice += float(price)
    currentMenuItem = MenuItem(description, price, id)
    currentOrder.append(currentMenuItem)

    return JsonResponse({'message': 'Item Added'})