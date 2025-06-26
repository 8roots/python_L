fh = open('mbox-short.txt')
print(fh)

for lx in fh:
    lx = lx.rstrip()
    print(lx.upper())
#首先文件每一行末尾都会有换行符,
#其次rint语句会自动添加一个换行符
#因此,使用rrstrip清除文件末尾的换行符
   