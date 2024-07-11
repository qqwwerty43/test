with open('circle.txt', 'r') as file:
    content = file.readlines()
    center = list(map(float, content[0].split(' ')))
    radius = float(content[1])

dots = []

with open('dot.txt', 'r') as file:
    content = file.readlines()
    for i in range(len(content)):
        dots.append(list(map(float, content[i].split(' '))))

for dot in dots:
    if (dot[0] - center[0]) ** 2 + (dot[1] - center[1]) ** 2 == radius ** 2:
        print('0')
    elif (dot[0] - center[0]) ** 2 + (dot[1] - center[1]) ** 2 < radius ** 2:
        print('1')
    else:
        print('2')