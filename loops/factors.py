num = int(raw_input('Enter an integer number: '))
factors = [0]
for i in range(1,num):
    if num % i == 0:
        factors.append(i)
print factors
