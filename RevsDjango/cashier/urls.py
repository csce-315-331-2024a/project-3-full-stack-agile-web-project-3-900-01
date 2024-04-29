from django.urls import path
from . import views

'''
This is the order page routing logic.
'''

urlpatterns = [
   
    path('', views.revs_cashier_screen, name='Revs-Cashier-Screen'),
    path('cashier_checkout/', views.cashier_checkout, name='cashier_checkout'),
    path('cashier_add_item/', views.cashier_add_item, name='cashier_add_item'),
    path('cashier_transaction_view/', views.cashier_transaction_view, name='cashier_transaction_view'),
    path('cashier_orders/', views.cashier_orders, name='cashier_orders'),
    path('cashier_get_cart_items/', views.cashier_get_cart_items, name='cashier_get_cart_items'),
    path('views.cashier_login_view/', views.cashier_login_view, name='views.cashier_login_view'),
    path('revs_order_management/', views.revs_order_management, name='revs_order_management'),
    path('cashier_remove_item/', views.cashier_remove_item, name='cashier_remove_item'),
    path('cashier_remove_all_items/', views.cashier_remove_all_items, name='cashier_remove_all_items'),
    path('cashier_text_to_speech/', views.cashier_text_to_speech, name='cashier_text_to_speech'),
]

 # path('', views.orders, name='Revs-Cashier-Screen'),
    # path('checkout/', views.checkout, name='cashierCheckout'),
    # path('add/', views.addItem, name='cashierAddItem'),
    # path('transaction/', views.transaction_view, name='cashierTransaction'),
    # path('orders/', views.transaction_view, name='cashierOrders'),
    # path('getCartItems/', views.get_cart_items, name='cashierGetCartItems'),
    # path('login/', views.login_view, name='cashierLogin'),
    # path('ordermanagement/', views.orderManagement, name='Revs-ordermanagement'),
    # path('removeItem/', views.removeItem, name='cashierRemoveItem'),
    # path('removeAllIems/', views.removeAllIems, name='cashierRemoveAllItems'),
    # path('textToSpeech/', views.textToSpeech, name='cashierTextToSpeech'),