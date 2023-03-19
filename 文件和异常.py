# with open('test.txt') as file_object:
#     concent=file_object.read()
# print(concent.rstrip())

file_path="D:/python学习/爬虫示例/test.txt"
# with open(file_path) as file_object:
#     lines=file_object.readlines()

# pi_string=''
# for line in lines:
#     pi_string+=line.rstrip()
#
# print(pi_string)
# print(len(pi_string))


'''写入文件'''
with open(file_path,'w') as file_object:
    file_object.write("I lover you!\n")
    file_object.write("xxiixi\n")

with open(file_path,'a') as aaa:
    aaa.write("jjjjj")