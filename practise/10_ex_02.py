'''统计每封邮件一天中各小时发送数。查找时间字符串，然后使用冒号字符将字符串分割成部分，
从而从“From”行中提取小时。一旦你累积了每个小时的计数，按小时排序打印出计数，每行一个，如下所示。
示例行：
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
python timeofday.py
输入文件名：mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1'''
fname = input('输入文件名：')
try:
    fhand = open(fname)
except FileNotFoundError:
    print(fname,'文件未找到')
    exit()#总是忘记输入exit()
lst= dict()
for lines in fhand:
    lines = lines.rstrip()
    if lines.startswith('From '):
        parts = lines.split()
        if len(lines) >= 2 :
            times = parts[5]
            '''
            try:
                hour = time_str.split(':')[0]
                hour_counts[hour] = hour_counts.get(hour, 0) + 1
            except IndexError:
                continue  # 跳过格式不正确的时间'''
            time = times.split(':')
            hour = time[0]
            # print(hour)
            lst[hour] =lst.get(hour,0)+1
# print(lst)

li = list(lst.items())
li.sort(reverse=False)
for key, val in li:
    print(key,val)



