height = int(input('Height? >> '))
width = int(input('Width? >> '))

print("Hollow Box Pattern")

for i in range(1, height + 1):
    for j in range(1, width + 1):
        if(i == 1 or i == height or j == 1 or j == width):
            print('*', end = ' ')
        else:
            print(' ', end = ' ')

    print()
