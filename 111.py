import  requests
img = requests.get('https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png')
with open('C:\\Users\\小可爱\Desktop\\东软-招商证券\\baidu.png','wb') as f:
    f.write(img.content)