import requests
from getpass import getpass
from datetime import datetime
import os

# 个人访问令牌
access_token = getpass('Enter your GitHub Access Token: ')

# GitHub 用户名
username = input('Enter your GitHub username: ')

# API 请求头部
headers = {
    'Authorization': f'token {access_token}',
    'Accept': 'application/vnd.github.v3.star+json',
}

# 初始化星标仓库列表
starred_repos = []

# 每页展示的仓库数量
per_page = 100  # GitHub API的最大值

# 初始页码
page = 1

# 循环获取所有页面的星标仓库
while True:
    response = requests.get(f'https://api.github.com/users/{username}/starred?per_page={per_page}&page={page}', headers=headers)
    repos = response.json()
    if not repos:
        break  # 当某一页没有仓库时，退出循环
    starred_repos.extend(repos)
    print(f"Collected {len(starred_repos)} repositories so far.")
    page += 1

# 提取星标仓库的相关信息
starred_repo_info = []
repo_names = []  # 仅包含仓库名的列表
for repo in starred_repos:
    repo_name = repo['repo']['full_name']
    repo_description = repo['repo']['description']
    starred_at_utc = datetime.strptime(repo['starred_at'], '%Y-%m-%dT%H:%M:%SZ')
    starred_at_local = starred_at_utc.strftime('%Y-%m-%d %H:%M:%S')  # 转换为本地时间的24小时制
    starred_repo_info.append({
        'name': repo_name,
        'description': repo_description,
        'starred_at': starred_at_local
    })
    repo_names.append(repo_name)

# 获取脚本所在的目录
script_directory = os.path.dirname(os.path.abspath(__file__))

# 将文件名与脚本目录结合
output_file_path = os.path.join(script_directory, 'starred_repos_info.txt')

# 将结果保存到文件
try:
    with open(output_file_path, 'w') as file:
        for repo_info in starred_repo_info:
            file.write(f"Repository: {repo_info['name']}\nDescription: {repo_info['description']}\nStarred at: {repo_info['starred_at']}\n\n")
        file.write("List of Repository Names:\n")
        file.write(str(repo_names))
except Exception as e:
    print("An error occurred:", e)

print(f"Starred repositories information saved to '{output_file_path}'")
