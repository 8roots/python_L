stuff = 'hello\nworld'
print(stuff)
i = len(stuff)
print(i)
count = 0
sum = 0
print('before', count,sum)
for thing in [9,41,12,3,74,15] :
	count = count + 1
	sum = sum + thing
	print(count ,sum, thing)
print ('after', count, sum, sum / count)