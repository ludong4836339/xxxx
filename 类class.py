# 创建dog类
# class Dog:
#     '''一次模拟小狗的简单尝试'''
#     def __int__(self,name,age):
#         '''初始化属性name和age'''
#         self.name=name
#         self.age=age
#
#     def sit(self):
#         '''模拟小狗收到命令时墩下'''
#         print(f"{self.name} is now sitting")
#
#     def roll_over(self):
#         '''模拟小狗收到命令时打滚'''
#         print(f"{self.age} rolled over!")
#
# my_dog=Dog("啊啊啊",11)

class Car:
    '''一次模拟汽车的简单尝试'''
    def __int__(self,make,modle,year):
        ''''初始化汽车属性'''
        self.make = make
        self.modle = modle
        self.year = year
        self.odometer_reading=0

    def get_describe_name(self):
        long_name=f"{self.make} {self.modle} {self.year}"
        return long_name.title()

my_new_car=Car('aidi','a4',2019)
print(my_new_car.get_describe_name())