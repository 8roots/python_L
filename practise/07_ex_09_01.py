#编写一个程序，通读一个文件并以全大写形式打印文件的内容（逐行）。
fhandle = open('mbox-short.txt','r')
f = fhandle.read()
for line in f :
    print(line.rstrip().upper())