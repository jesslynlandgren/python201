h = int(raw_input('Height: '))
max_width = h + (h-1)
start = max_width/2 + 1

full = ' '*max_width
full2 = []

for i in range(0,max_width + 1):
    full2.append(" ")

for i in range(0,h):
    full[start - i:start + i] = '*'
    print start


# Keyur's solution
# for i in range(1,(h*2),2):
#     for j in range(i,i+1):
#         print j
#         print h - (i/2)
#         print " " * (h - (i/2)) + ("*" * j)
