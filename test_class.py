# #创建一个人类
# #通过class关键字，定义一个类
# class Person:
#     name="default"
#     age=0
#     gender='male'
#     weight=0
#
#
#     def set_param(self,name):
#         self.name=name
#     def set_age(self,age):
#         self.age=age
#     def eat(self):
#         print("eating")
#
#     def play(self):
#         print("playing")
#
#     def jump(self):
#         print("jump")
#
# zs=Person()
# zs.set_param('zhangsan')
# zs.set_age(20)
# print(f"zhangsan的姓名是：{zs.name},张三的年龄是{zs.age}")
# print(zs.name)
import pytest
class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name #.title()

my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())


