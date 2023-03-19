import  json

# number=[2,3,4,5,6,7,8]
# file_name="number_json"
# # with open(file_name,'w') as f:
#     # json.dump(number,f)
#
# with open(file_name) as f:
#     number=json.load(f)
# print(number)

# 保存和读取用户生成的数据

# uesename=input('What is your name？按回车结束')
filename='username.json'
# with open(filename,'a') as f:
#     json.dump(uesename,f)
#     print(f"Well remeber you when you come back,{uesename}\n")

with  open(filename) as f:
    aaa=json.load(f)
    print(aaa)