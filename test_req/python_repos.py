import  requests

# 执行API调用并存为响应
url='https://api.github.com/search/repositories?q=language:python&sort=starts'
headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code:{r.status_code}")
# 将API响应赋给一个变量
requests_dict = r.json()
print(f"Total repositeries :{requests_dict['total_count']}")

#搜索有关仓库的信息
repo_dicts = requests_dict['items']
print(f"Repositories returned:{len(repo_dicts)}")
#研究第一个仓库
repo_dict = repo_dicts[0]
print(f"\nKeys:{len(repo_dict)}")
for key in sorted(repo_dict.keys()):  # 遍历所有的字典
    print(key)

print(f"Nmae:{repo_dict['name']}")
print(f"Owner:{repo_dict['owner']['login']}")
print(f"Stars:{repo_dict['stargazers_count']}")
print(f"Repository:{repo_dict['html_url']}")

# 处理结果
# print(requests_dict.keys())