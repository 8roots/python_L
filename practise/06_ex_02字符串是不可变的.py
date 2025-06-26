# 很诱人地想在赋值语句的左侧使用 [] 运算符，意图改变字符串中的一个字符。例如：

grtt = 'Hello, world!'
# grtt[0] = 'J'
# TypeError: 'str' object does not support item assignment

# 这种情况下的“对象”是字符串，“项目”是你试图赋值的字符。目前，对象 (object) 与值的含义相同，但我们稍后会完善这个定义。项目 (item) 是序列中的值之一。

# 出现错误的原因是字符串是不可变的 (immutable)，这意味着你不能更改现有的字符串。你能做的最好的事情是创建一个新字符串，它是原始字符串的变体：

grtt = 'Hello, world!'
new_greeting = 'J' + grtt[1:]
print(new_greeting)
#为什么[1：]里明明是1，不是应该替代字母e吗？
'''
🔍 解读 [1:] 的含义：

    字符串中的索引是从 0 开始 的：

Index:     0 1 2 3 4 5 6 7 ...
String:    H e l l o ,   w ...

grtt[1:] 表示：从索引 1 开始到结尾的子字符串，不包括索引 0 的字符（即 'H' 被丢掉了）：

    grtt[1:]  ➜  'ello, world!'

🔁 替换首字母：

所以，'J' + grtt[1:] 的效果是：

'J' + 'ello, world!'  ➜  'Jello, world!'

它 用 'J' 替换了原本的首字母 'H'，但并没有直接修改原字符串（因为字符串是不可变的），而是创建了一个新字符串。
✅ 输出：

Jello, world!

🔚 总结：

    grtt[1:] 是从 第二个字符开始。

    所以你拼接 'J' + grtt[1:] 实际上是“替换第一个字符”的简便方法。'''