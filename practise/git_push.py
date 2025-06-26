
import os
import sys
def run_command(cmd):
    print(f"执行: {cmd}")
    ret = os.system(cmd)
    if ret != 0:
        print(f"命令执行失败，退出码: {ret}")
        sys.exit(1)
def main():
    # 检查当前目录是否是Git仓库
    if os.system("git rev-parse --is-inside-work-tree") != 0:
        print("错误：当前目录不是Git仓库！")
        sys.exit(1)
    
    # 获取当前分支
    current_branch = os.popen("git symbolic-ref --short HEAD").read().strip()
    print(f"当前分支: {current_branch}")
    
    # 显示状态
    run_command("git status -s")
    
    # 检查是否有更改
    if not os.popen("git status --porcelain").read().strip():
        print("没有需要提交的更改。")
        return
    
    # 输入提交信息
    commit_message = input("请输入提交信息（默认为'自动提交'）: ") or "自动提交"
    
    # 添加所有更改
    run_command("git add .")
    
    # 提交
    run_command(f"git commit -m \"{commit_message}\"")
    
    # 推送
    if os.system(f"git push origin {current_branch}") != 0:
        print("推送失败！")
        if input("尝试强制推送？(y/n) ").lower() == 'y':
            run_command(f"git push --force origin {current_branch}")
        else:
            print("推送已取消。")
    else:
        print("推送成功！")
    
    # 显示最终状态
    run_command("git status -s")
if __name__ == "__main__":
    main()
