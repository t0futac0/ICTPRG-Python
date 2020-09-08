#base_size=10
#for count in range (base_size):
#    for y in range(count+1):
#        print('x', end='')
#    print('')


base_size = 1

for count in range (base_size):
    for y in range (count * count):
        print('x', end='')
    print('')