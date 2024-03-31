import json
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.db import connection

# Global variables for tracking order information
currentPrice = 0.0
currentOrder = []
orderID = 1


# Class to store all information on a menu item
class MenuItem:
    def __init__(self, description, price, id, category):
        self.description = description
        self.price = price
        self.id = id
        self.category = category


# Initializes all the menu items buttons
def orders(request):
    global orderID

    with connection.cursor() as cursor:
        #gets next order id
        cursor.execute("SELECT MAX(id) FROM orders")
        orderID = cursor.fetchone()[0] + 1

        # Gets a list of all the menu items and sorts in alphabetical order
        cursor.execute("SELECT description, price, id, category FROM menu_items")
        data = cursor.fetchall()
        data.sort()
        buttonData = [{'description': currentItem[0], 'price': currentItem[1], 'id': currentItem[2],
                        'category': currentItem[3]} for currentItem in data]

        # Categorize buttons based on their descriptions
        categorizedButtons = {
            'Burgers': [],
            'Value Meals': [],
            'Sandwiches': [],
            'Shakes': [],
            'Beverages': [],
            'Sides': []
        }

        for button in buttonData:
            if button['category'] == 'Burger':
                categorizedButtons['Burgers'].append(button)
            elif button['category'] == 'Value Meal':
                categorizedButtons['Value Meals'].append(button)
            elif button['category'] == 'Sandwiches':
                categorizedButtons['Sandwiches'].append(button)
            elif button['category'] == 'Shakes/More':
                categorizedButtons['Shakes'].append(button)
            elif button['category'] == 'Drink':
                categorizedButtons['Beverages'].append(button)
            else:
                categorizedButtons['Sides'].append(button)

        context = {'categorizedButtons': categorizedButtons}

        return render(request, 'orders/orders.html', context)


# Adds menu item button functionality
def addItem(request):
    global currentPrice
    global currentOrder

    # Extracts all the menu item's information
    data = json.loads(request.body)
    description = data.get('description')
    price = data.get('price')
    id = data.get('id')
    category = data.get('category')

    # Updates all the global variables for the order
    currentPrice += float(price)
    currentMenuItem = MenuItem(description, price, id, category)
    currentOrder.append(currentMenuItem)

    return JsonResponse({'message': 'Item Added'})

#adds order placement functionality
def payNow(request):
    customerID = 1
    employeeID = 1111
    orderTime = "1/1/2024 9:00"

    #list of all food items in order
    foodItems = []
    for menuItem in currentOrder:
        foodItems += menuItem.id

    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO orders (order_id, customer_id, employee_id, total_price, order_time) VALUES (%s, %s, %s, %s, %s)",
            [orderID, customerID, employeeID, currentPrice, orderTime]
        )
        for foodItem in foodItems:
            cursor.execute(
                "INSERT INTO order_breakout (order_id, food_items) VALUES (%s, %s)",
                [orderID, foodItem]
            )
    return JsonResponse({'message': 'Checked Out'})

def cart_view(request):
    # Your logic to retrieve the shopping cart items and process the request goes here
    # For now, let's just render the empty cart.html template
    return render(request, 'orders/cart.html')
