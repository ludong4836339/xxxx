import requests
from plotly import offline
from plotly.graph_objs import bar
import  requests

# 执行API调用并存为响应
url='https://api.github.com/search/repositories?q=language:python&sort=starts'
headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
# print(f"Status code:{r.status_code}")
# 将API响应赋给一个变量
repo_dict = r.json()
repo_dicts =repo_dict['items']
repo_names,stars = [] , []
for repo_dict in  repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    # 可视化
data = [{
    'type':'bar',
    'x':repo_names,
    'y':stars
}]

my_layout ={
    'title':'GitHub上最受欢迎的Python项目',
    'xaxis':{'title':'Repository'},
    'yaxis':{'title':'Stars'},
}
fig= {'data':data,'layout':my_layout}
offline.plot(fig,filename='python_repos.html')