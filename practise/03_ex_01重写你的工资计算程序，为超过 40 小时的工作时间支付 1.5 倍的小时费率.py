hour = float(input('Enter Hour: '))
rate = float(input('your Rate: '))
more_hour = hour - 40
more_pay = rate*1.5
if hour > 40 :
    pay = more_pay*more_hour + ((hour - more_hour) * rate)
    print(pay)
else:
#    pay = (hour - more_hour) * rate
    pay = hour * rate
    print(pay)
print()

#   Ai优化后：
try:
    hour = float(input('Enter Hours Worked: '))
    rate = float(input('Enter Hourly Rate: '))
    
    if hour < 0 or rate < 0:
        print("Error: Values cannot be negative")
    elif hour > 40:
        overtime = hour - 40
        pay = (40 * rate) + (overtime * rate * 1.5)
        print(f"Pay: ${pay:.2f}")
        #        :.2f 表示保留2位小数
    else:
        pay = hour * rate
        print(f"Pay: ${pay:.2f}")
        
        
except ValueError:
    print("Error: Please enter valid numbers")