import subprocess

# 定义要运行的命令
command = "git branch --show-current"

# 使用subprocess运行命令
try:
    output = subprocess.check_output(command, shell=True, text=True)
    print("当前分支名称:", output.strip())
except subprocess.CalledProcessError:
    print("命令运行失败，请确保你在Git仓库中并且已安装Git。")
except Exception as e:
    print("发生了错误:", e)
