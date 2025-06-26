'''练习 4：找出文件中所有唯一的单词

莎士比亚在他的作品中使用了超过 20,000 个单词。
但你将如何确定这一点？你将如何生成莎士比亚使用的所有单词的列表？
你会下载他所有的作品，阅读它们，然后手动跟踪所有唯一的单词吗？

让我们改用 Python 来实现这一点。
列出存储在文件 romeo.txt（包含莎士比亚作品的一个子集）中所有按字母顺序排序的唯一单词。

首先，下载文件副本 www.py4e.com/code3/romeo.txt。
创建一个将包含最终结果的唯一单词列表。
编写一个程序打开文件 romeo.txt 并逐行读取。
对于每一行，使用 split 函数将该行分割成单词列表。
对于每个单词，检查该单词是否已在唯一单词列表中。
如果该单词不在唯一单词列表中，则将其添加到列表中。
程序完成后，按字母顺序排序并打印唯一单词列表。'''
fhandle = open('romeo.txt')
world = list()
for line in fhandle:
    # print('debug: ',line)
    for t in line.split():
        print('debug: ',t)
        if  t in world:
            continue
        else:
            world.append(t)
world.sort()
print(world)
