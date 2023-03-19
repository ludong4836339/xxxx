# # 定义一个函数  def
# def great_user():
#     '''显示简单的问候语'''
#     print('hello')
#  #  调用函数
# great_user()
#
# #   向函数传递参数
# def greet_user(username):    # 形参
#     """显示简单的问候语"""
#     print(f"hello,{username.title()}")
# greet_user('jess')         #    实参
#
# # 传递实参
# def describe_pet(anima_type,pet_name):
#     """显示宠物信息"""
#     print(f"\nI have a {anima_type}")
#     print(f"My {anima_type} is name is {pet_name}")
# describe_pet("狗","旺财")
# describe_pet("猫","咪咪")
#
# def describe_pet(anima_type,pet_name="xoxo"):
#     """显示宠物信息"""
#     print(f"\nI have a {anima_type}")
#     print(f"My {anima_type} is name is {pet_name}")
# describe_pet(anima_type="doddo")
#
# #  返回值 return
# def get_formatted_name(first_name,last_name):
#     """返回整洁的姓名"""
# # full_name=f"{first_name} {last_name}"
# # return full_name.title()
# # musician=get_formatted_name("张","四")
# # print(musician)
#
# # 传递任意数量的实参
# # def make_pizza(*toppings):
# #     '''打印顾客点的所有配料'''
# #     print(toppings)
# # make_pizza("洋葱")
# # make_pizza('ss','dada','qqq')
#
# def make_pizza(*toppings):
#     '''告诉要在制作的比萨'''
#     print(f"\nMake a pizza whit the following toppings:")
#     for topping in toppings:
#         print(f"-{topping}")
# make_pizza("洋葱")
# make_pizza('ss','dada','qqq')
# 导入整个模块
def make_pizza(siza,*toppings):
     '''概述要制作的披萨'''
     print(f"\nMake a {siza} -inch pizza whit the folowing toppings:")
     for topping in toppings:
         print(f"-{topping}")
