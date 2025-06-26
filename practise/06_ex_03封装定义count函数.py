# word = 'banana'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
# print(count)
'''
这个程序演示了另一种称为计数器 (counter) 的计算模式。变量 count 初始化为 0，然后在每次找到“a”时递增。
当循环退出时，count 包含结果：a 的总数。

练习 3： 将此代码封装在一个名为 count 的函数中，并对其进行通用化，使其接受字符串和字母作为参数。'''

'''
自己写的
def count(word):
    count = 0
    strs = str(word)
    zimu = input('zimu:')
    for letter in strs.lower():
        if letter == zimu:
            count = count + 1
    return(count)

word = input('输入：')
num = count(word)
print(num)
'''
#ai写的
def count(word, target_char):
    """
    计算字符串中特定字符的出现次数（不区分大小写）
    
    参数:
        word (str): 要搜索的字符串
        target_char (str): 要计数的字符
        
    返回:
        int: 目标字符出现的次数
    """
    count = 0
    for letter in word.lower():
        if letter == target_char.lower():
            count += 1
    return count

# 使用示例
user_input = input('请输入字符串: ')
char_to_count = input('请输入要统计的字符: ')

result = count(user_input, char_to_count)
print(f"字符 '{char_to_count}' 出现的次数: {result}")