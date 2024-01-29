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