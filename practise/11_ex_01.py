'''
练习 1： 编写一个简单的程序来模拟 Unix 上的 grep 命令的操作。
要求用户输入一个正则表达式，并计算匹配该正则表达式的行数：

$ python grep.py
输入一个正则表达式: ^Author
mbox.txt 有 1798 行匹配 ^Author

$ python grep.py
输入一个正则表达式: ^X-
mbox.txt 有 14368 行匹配 ^X-

$ python grep.py
输入一个正则表达式: java$
mbox.txt 有 4175 行匹配 java$
'''
import re

def grep_count(pattern, filename):
    """统计文件中匹配正则表达式的行数"""
    count = 0
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if re.search(pattern, line):
                count += 1
    return count

if __name__ == "__main__":
    # 用户输入正则表达式
    regex = input("输入一个正则表达式: ")
    filename = "mbox-short.txt"  # 替换为你的文件名

    try:
        # 计算匹配行数
        matched_lines = grep_count(regex, filename)
        print(f"{filename} 有 {matched_lines} 行匹配 {regex}")
    except FileNotFoundError:
        print(f"错误：文件 {filename} 未找到")
    except re.error:
        print("错误：无效的正则表达式")


