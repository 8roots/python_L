#!/bin/bash

# 一键 Git 推送脚本
# 功能：自动添加、提交和推送所有更改到远程仓库

# 设置颜色代码
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # 无颜色

# 检查是否在 Git 仓库中
if ! git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
    echo -e "${RED}错误：当前目录不是 Git 仓库！${NC}"
    exit 1
fi

# 获取当前分支
current_branch=$(git symbolic-ref --short HEAD)

# 显示仓库状态
echo -e "${YELLOW}=== Git 仓库状态 ==="
git status -s
echo -e "========================${NC}"

# 检查是否有更改需要提交
if [ -z "$(git status --porcelain)" ]; then
    echo -e "${GREEN}没有需要提交的更改。${NC}"
    exit 0
fi

# 获取用户输入提交信息
read -p "请输入提交信息（默认为'自动提交'）: " commit_message
commit_message=${commit_message:-"自动提交"}

# 添加所有更改
echo -e "${YELLOW}添加所有更改...${NC}"
git add .

# 提交更改
echo -e "${YELLOW}提交更改...${NC}"
git commit -m "$commit_message"

# 推送到远程仓库
echo -e "${YELLOW}推送到远程仓库 (分支: $current_branch)...${NC}"
git push origin "$current_branch"

# 检查推送结果
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ 推送成功！${NC}"
else
    echo -e "${RED}✗ 推送失败！${NC}"
    echo -e "${YELLOW}尝试强制推送？(y/n)${NC}"
    read force_push
    if [ "$force_push" = "y" ] || [ "$force_push" = "Y" ]; then
        git push --force origin "$current_branch"
        echo -e "${GREEN}✓ 强制推送成功！${NC}"
    else
        echo -e "${YELLOW}推送已取消。${NC}"
    fi
fi

# 显示最终状态
echo -e "\n${YELLOW}=== 最终状态 ==="
git status -s
echo -e "================${NC}"