# zip returns an iterator that combines multiple iterables into one sequence of tuples
# each tuple contains the elements in that position from all the iterables

letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))

# unzip using *

some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)
print(some_list)

# enumerate is a built in function that returns an iterator of tuples containing indices and values of a list

letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)

# coordinates with a label

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []

for point in zip(labels, x_coord, y_coord, z_coord):
    points.append('{}: {}, {}, {}'.format(*point))

for point in points:
    print(point)

# create a dictionary with zip

cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))
print(cast)

# unzip tuples

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

names, heights = zip(*cast)

print(names)
print(heights)

# transpose with zip

data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))
print(data_transpose)

# enumerate for modifying a list

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

for i, character in enumerate(cast):
    cast[i] = character + ': ' + str(heights[i])

print(cast)