#!/bin/bash

# 一键 Git 推送脚本
# 功能：自动添加、提交和推送所有更改到远程仓库
# 版本：2.0

# 设置颜色代码
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # 无颜色

# 错误处理函数
error_exit() {
    echo -e "${RED}$1${NC}" >&2
    exit 1
}

# 检查是否在 Git 仓库中
if ! git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
    error_exit "错误：当前目录不是 Git 仓库！"
fi

# 获取当前分支（简化方式）
current_branch=$(git branch --show-current 2>/dev/null)
if [ -z "$current_branch" ]; then
    error_exit "错误：当前处于分离头指针状态，不在任何分支上！"
fi

# 显示仓库状态
echo -e "${CYAN}=== Git 仓库状态 ==="
git status -s
echo -e "========================${NC}"

# 检查是否有更改需要提交
if [ -z "$(git status --porcelain)" ]; then
    echo -e "${GREEN}没有需要提交的更改。${NC}"
    exit 0
fi

# 获取用户输入提交信息
while true; do
    read -p "请输入提交信息（不能为空）: " commit_message
    if [ -n "$commit_message" ]; then
        break
    fi
    echo -e "${YELLOW}提交信息不能为空，请重新输入。${NC}"
done

# 添加所有更改（包括子目录）
echo -e "${CYAN}添加所有更改...${NC}"
git add -A || error_exit "添加更改失败！"

# 检查添加后是否有可提交内容
if [ -z "$(git diff --cached --name-only)" ]; then
    echo -e "${YELLOW}没有检测到可提交的更改（可能是文件被忽略）。${NC}"
    exit 0
fi

# 提交更改
echo -e "${CYAN}提交更改...${NC}"
git commit -m "$commit_message" || error_exit "提交失败！"

# 推送到远程仓库
echo -e "${CYAN}推送到远程仓库 (分支: $current_branch)...${NC}"

# 尝试推送并处理错误
if ! git push origin "$current_branch" 2> push_error.log; then
    # 捕获错误信息
    push_error=$(<push_error.log)
    rm -f push_error.log
    
    # 检查是否缺少上游分支
    if [[ "$push_error" == *"has no upstream branch"* ]]; then
        echo -e "${YELLOW}未设置上游分支，正在设置并推送...${NC}"
        if git push --set-upstream origin "$current_branch"; then
            echo -e "${GREEN}✓ 推送成功（已设置上游分支）！${NC}"
        else
            error_exit "设置上游分支失败！"
        fi
    else
        echo -e "${RED}✗ 推送失败！${NC}"
        echo -e "${YELLOW}错误详情：${push_error}${NC}"
        
        # 检查是否为保护分支（使用精确匹配）
        protected_branches=("main" "master" "develop")
        if printf '%s\n' "${protected_branches[@]}" | grep -q "^${current_branch}$"; then
            echo -e "${RED}警告：${current_branch} 是保护分支，禁止强制推送！${NC}"
            exit 1
        fi
        
        # 显示远程差异
        echo -e "\n${CYAN}=== 远程差异 ==="
        git fetch --quiet
        git diff --name-status "origin/$current_branch"..HEAD
        echo -e "================${NC}"
        
        # 询问强制推送
        echo -e "${YELLOW}尝试强制推送？(y/n)${NC}"
        read -r force_push
        if [[ "$force_push" =~ ^[Yy]$ ]]; then
            echo -e "${YELLOW}⚠️ 警告：强制推送会覆盖远程更改！${NC}"
            read -r -p "确认强制推送？(输入 'CONFIRM' 大写确认): " confirm_force
            if [ "$confirm_force" == "CONFIRM" ]; then
                if git push --force-with-lease origin "$current_branch"; then
                    echo -e "${GREEN}✓ 强制推送成功！${NC}"
                else
                    error_exit "强制推送失败！"
                fi
            else
                echo -e "${YELLOW}推送已取消。${NC}"
                exit 0
            fi
        else
            echo -e "${YELLOW}推送已取消。${NC}"
            exit 0
        fi
    fi
else
    echo -e "${GREEN}✓ 推送成功！${NC}"
fi

# 显示最终状态
echo -e "\n${CYAN}=== 最终状态 ==="
git status -s
echo -e "================${NC}"