try:
    hour = float(input('Enter Hour: '))
    rate = float(input('Enter Rate: '))
    if hour < 0 or rate < 0:
        print('Error: Values cannot be Negetive')
    elif hour > 40:
        overtime= hour - 40
        pay = (40*rate)+(overtime*1.5*rate)
        print(f'pay: ${pay:.2f}')
    else:
        pay = hour * rate
        print(f'pay: ${pay:.2f}')
        
except ValueError:
    print('Error: Please enter valid numbers')