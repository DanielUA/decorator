# from time import sleep
# import datetime
# from typing import Any


# def timing(func):
#     def wrapper(*args, **kwargs):
#         start_func = datetime.datetime.now()
#         result = func(*args, **kwargs)
#         finish_func = datetime.datetime.now()
#         print(finish_func - start_func)
#         return result 
#     return wrapper

# def time_all_class_methods(cls):
#     class NewCls(object):
#         def __init__(self, *args, **kwargs):
#             self.oIstance = cls(*args, **kwargs)
        
#         def __getattribute__(self, item):
#             try:
#                 attr = super(NewCls, self).__getattribute__(item)
#             except AttributeError:
#                 pass
#             else:
#                 return attr
#             attr = self.oIstance.__getattribute__(item)
#             if type(attr) == type(self.__init__):
#                 return timing(attr)
#             else:
#                 return attr
            

#     return NewCls
        

# @time_all_class_methods
# class Foo(object):
#     @timing
#     def foo_func(self):
#         print("Start")
#         sleep(2)
#         print("End")
#     @timing
#     def foo_2_func(self):
#         print("Start")
#         sleep(3)
#         print("End")

# test = Foo()

# test.foo_2_func()
# test.foo_func()   


"""---------------------------------------"""

# class KeyStore:
#     def __init__(self, name, password):
#         self.__password = None
#         self.__secret = None
#         self.name = name
#         self.password = password


#     @property
#     def password(self):
#         print("No wway to get your password")
        

#     @password.setter
#     def password(self, value):
#         if self.__password is None:
#             self.__password = value
#         else:
#             if self.validate():
#                 print("Password corect")
#                 self.__password = value
#             else:
#                 print("Incorrect")


#     @property  
#     def secret(self):
#         if self.validate():
#             return self.__secret


#     @secret.setter
#     def secret(self, value):
#         if self.validate():
#             self.__secret = value


#     def validate(self):
#         value = input("Password: ")
#         if self.__password == value:
#             print("Ok")
#             return True
#         print("Wrong password")
#         return False
    

# k_store = KeyStore("Dan", "12345")
# k_store.password = '111'
# print(k_store.password)
# k_store.password = "56890"
# k_store.secret = 'TEST'
# print(k_store.secret)    


"""---------------------------------------"""
from uuid import uuid1

class NoeEnoughRights(Exception):
    def __init__(self, *value):
        self.value = value


    def __str__(self):
        return "Yon haven`t enough rights fo this" + repr(self.value)


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self, id_=None):
        if id_ is None:
            id_ = uuid1().int 
        self.id = id_
        self.items = list()
        self.total = 0


    def __add__(self, item):
        self.items.append(item)
        self.total += item.price


    def __sub__(self, item):
        if item in self.items:
            self.items.remove(item)
            self.total -= item.price


    def __str__(self):
        msg = "Items\n"
        if self.items:
            for item in self.items:
                msg += f"{item.name}:{item.price}\n"
        msg += f"Total: {self.total}"
        return msg
    
class Person:
    def add(self, *args):
        raise NoeEnoughRights


    def sub(self, *args):
        raise NoeEnoughRights


    def view(self, *args):
        raise NoeEnoughRights


    def check(self, *args):
        raise NoeEnoughRights


    def confirm(self, *args):
        raise NoeEnoughRights


    def complete(self, *args):
        raise NoeEnoughRights


class Customer(Person):
    def view(self, order):
        return str(order)
    
class Seller(Person):
    def add(self, item, order=None):
        if order is None:
            order = Order()
        order + item
        return order


    def sub(self, item, order):
        order - item


    def view(self, order):
        return str(order)


    def confirm(self, order, manufacturer):
        manufacturer.add(order)


class Manufacturer(Person):
    def __init__(self):
        self.orders = dict() 


    @property
    def order_list(self):
        return list(self.orders.keys())
    
    def add(self, order):
        self.orders[order.id] = False

    def view(self, order):
        if order.id in self.orders:
            return self.orders[order.id]
    
    def complete(self, order):
        if order.id in self.orders:
            self.orders[order.id] = True

ball = Item("Ball", 10)
cup = Item("Cup", 5)
bag = Item("Bag", 15)

seller = Seller()
customer = Customer()
manufacturer = Manufacturer()

new_order = seller.add(ball)
print(seller.view(new_order))
print(customer.view(new_order))

seller.add(cup, new_order)
print(customer.view(new_order))

seller.sub(cup, new_order)
print(customer.view(new_order))

seller.add(bag, new_order)
print(customer.view(new_order))

seller.confirm(new_order, manufacturer)
print(manufacturer.order_list)
print(manufacturer.view(new_order))
manufacturer.complete(new_order)
print(manufacturer.view(new_order))
