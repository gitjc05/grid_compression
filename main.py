import random
import numpy as np

##JamBoard


arr2d = [
    [0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [0, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 1],
]


init = 81


arr2d = []


for y in range(init):
    row = []
    for x in range(init):
        row.append(random.randint(0, 1))
    arr2d.append(row)
    



inital_height = len(arr2d)  # 6
inital_width = len(arr2d[0])  # 6


width = 3
height = 3


width_slice = []  # [[start1, end1], [start2, end2]]
height_slice = []  # [[start1, end1], [start2, end2]]


start_w = 0
end_mult = 1

for i in range(width):
    start = start_w
    end = inital_width / width
    end *= end_mult
    width_slice.append([int(start), int(end)])

    start_w = end
    end_mult += 1


start_h = 0
end_mult = 1

for i in range(height):
    start = start_h
    end = inital_height / height
    end *= end_mult
    height_slice.append(list(range(int(start), int(end))))

    end_mult += 1
    start_h = end


final_2darr = []  # [[1, 2, 3....], [2, 3,1, ..]]


# height_slice = [[0, 1, 2], [3, 4, 5]]


# width_slice = [[0, 3], [3, 6]]


for cRow in height_slice:
    for cCol in width_slice:
        pixels = []
        for row in cRow:
            pixels.extend(arr2d[row][cCol[0] : cCol[1]])

        final_2darr.append(pixels)


final_2b2 = []


i = 0

end_h = width

end_w = width + height


def ave(l_type):
    return sum(l_type) / len(l_type)


i = 0

for x in range(height):
    row = []
    for y in range(width):
        row.append(ave(final_2darr[i]))
        i += 1
    final_2b2.append(row)




for row in arr2d:
    print(row)


for row in final_2b2:
    print(row)
