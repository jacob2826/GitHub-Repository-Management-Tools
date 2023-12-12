import requests
from getpass import getpass

# 个人访问令牌
access_token = getpass('Enter your GitHub Access Token: ')

# API 请求头部
headers = {
    'Authorization': f'token {access_token}',
    'Accept': 'application/vnd.github.v3+json',
}

# 要删除的仓库列表
# 格式应为 '用户名/仓库名'
repos_to_delete = [
    'username/repo1',
    'username/repo2',
    # 在这里添加更多仓库
]

# 遍历并删除指定的仓库
for repo_name in repos_to_delete:
    print(f'Deleting repo {repo_name}...')
    delete_response = requests.delete(f'https://api.github.com/repos/{repo_name}', headers=headers)

    if delete_response.status_code == 204:
        print(f'Repo {repo_name} deleted successfully.')
    else:
        print(f'Failed to delete repo {repo_name}. Status code: {delete_response.status_code}')

print("Specified repos have been deleted.")
