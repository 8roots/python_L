#字典的一个常见用途是统计文件中某些书面文本中单词的出现次数。
'''
我们将编写一个 Python 程序来通读文件的行，将每行分解成单词列表，然后遍历该行中的每个单词，并使用字典对每个单词进行计数。

你会看到我们有两个 for 循环。外层循环读取文件的行，内层循环遍历该特定行上的每个单词。这是称为嵌套循环 (nested loops) 的模式的一个例子，因为其中一个循环是外层循环，另一个循环是内层循环。

因为每次外层循环进行一次迭代时，内层循环都会执行其所有迭代，所以我们认为内层循环迭代得“更快”，而外层循环迭代得更慢。

两个嵌套循环的组合确保我们将计算输入文件中每一行的每一个单词。
'''
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)

# 代码: https://www.py4e.com/code3/count1.py
'''由于 Python 的 split 函数查找空格并将单词视为由空格分隔的标记
因此我们会将单词“soft!”和“soft”视为不同的单词，并为每个单词创建单独的字典条目。
此外，由于文件包含大写字母，我们会将“who”和“Who”视为具有不同计数的不同单词。'''
#我们可以通过使用字符串方法 lower、punctuation 和 translate 来解决这两个问题。
# translate 是这些方法中最微妙的一个。以下是 translate 的文档：
'''
line.translate(str.maketrans(fromstr, tostr, deletestr))
'''
#将 fromstr 中的字符替换为 tostr 中相同位置的字符，并删除所有在 deletestr 中的字符。
# fromstr 和 tostr 可以是空字符串，deletestr 参数可以省略。
#我们不会指定 tostr，但我们将使用 deletestr 参数来删除所有标点符号。
import string

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    # 前两个参数是空字符串
    line = line.translate(line.maketrans("", "", string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)

# 代码: https://www.py4e.com/code3/count2.py
'''浏览这个输出仍然很麻烦，
我们可以使用 Python 来精确地得到我们正在寻找的东西，
但要做到这一点，我们需要学习 Python 的元组。
一旦我们学习了元组，我们将继续这个例子。'''