import requests
from getpass import getpass

# 个人访问令牌
access_token = getpass('Enter your GitHub Access Token: ')

# GitHub 用户名
username = input('Enter your GitHub username: ')

# API 请求头部
headers = {
    'Authorization': f'token {access_token}',
    'Accept': 'application/vnd.github.v3+json',
}

# 初始化仓库列表
all_repos = []

# 每页展示的仓库数量
per_page = 100  # 可以设置为100，这是GitHub API的最大值

# 初始页码
page = 1

# 循环获取所有页面的仓库
while True:
    response = requests.get(f'https://api.github.com/users/{username}/repos?visibility=public&per_page={per_page}&page={page}', headers=headers)
    repos = response.json()
    if not repos:
        break  # 当某一页没有仓库时，退出循环
    all_repos.extend(repos)
    page += 1

# 打印所有公开的仓库名称
for repo in all_repos:
    print(repo['full_name'])
