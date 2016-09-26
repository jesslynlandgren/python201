w = int(raw_input('Width: '))
h = int(raw_input('Height: '))

for i in range(0,h):
    if i == 0 or i == (h-1):
        print '*'*w
    else:
        print '*' + (' '*(w-2)) + '*'
