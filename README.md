# GitHub Repository Management Tools

> **声明**: 本项目（包括此README文件）90%的内容都是由ChatGPT-4生成的，感谢OpenAI改变世界。

这个项目提供了4个Python脚本，用于管理GitHub上的仓库。以下是各个脚本的功能描述：

## 功能

- `list_public_repos.py`: 列出您在GitHub上的所有公开仓库。
- `delete_specified_repos.py`: 批量删除您指定的仓库。
- `list_star_repos.py`: 列出您在GitHub上star过的所有仓库，包括每个仓库的描述和star时间。
- `unstar_specified_repos.py`: 批量取消对指定仓库的star。

## 安装

在使用这些脚本之前，您需要确保Python已安装在您的计算机上。您可以访问 [Python官网](https://www.python.org/downloads/) 下载并安装最新版本的Python。

此外，您还需要安装`requests`库，可以通过以下命令安装：

```bash
pip install requests
```

## 获取GitHub个人访问令牌

要使用这些脚本，您需要一个GitHub个人访问令牌。您可以按照以下步骤获取：

1. 登录您的GitHub账户。
2. 点击右上角的头像，然后选择"Settings"。
3. 在侧边栏中，选择"Developer settings"。
4. 在"Personal access tokens"部分，点击"Generate new token"。
5. 给您的token命名，并为其分配适当的权限。对于这些脚本，您至少需要“repo”权限。
6. 点击"Generate token"，并复制生成的token。

请妥善保管您的token，不要在不安全的地方存储或分享。

## 使用方法

1. **列出所有公开仓库**:
   - 运行`list_public_repos.py`。例如：`python list_public_repos.py`。
   - 按照提示输入您的GitHub用户名和个人访问令牌。
   - 脚本将列出您所有的公开仓库。

2. **删除指定仓库**:
   - 在`delete_specified_repos.py`中指定您想要删除的仓库列表。
   - 运行`delete_specified_repos.py`。例如：`python delete_specified_repos.py`。
   - 按照提示输入您的GitHub个人访问令牌。
   - 脚本将删除列表中指定的仓库。

3. **列出所有star过的仓库**:
   - 运行`list_star_repos.py`。例如：`python list_star_repos.py`。
   - 按照提示输入您的GitHub用户名和个人访问令牌。
   - 脚本将列出您star过的所有仓库，包括每个仓库的描述和star时间。

4. **取消star指定仓库**:
   - 在`unstar_specified_repos.py`中指定您想要取消star的仓库列表。
   - 运行`unstar_specified_repos.py`。例如：`python unstar_specified_repos.py`。
   - 按照提示输入您的GitHub个人访问令牌。
   - 脚本将取消列表中指定仓库的star。

## 注意事项

- 使用这些脚本时，请确保您了解它们的操作。删除仓库的操作是不可逆的。
- 在使用脚本前仔细检查仓库列表，确保不会误删重要的仓库。
- 保护您的个人访问令牌，不要在脚本中硬编码或在不安全的地方存储。

## 贡献

如果您有任何建议或改进，欢迎通过Pull Requests或Issues与我分享。

## 许可

[MIT](LICENSE)
