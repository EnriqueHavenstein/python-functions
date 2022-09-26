# booleans

a = (10 == 9)
b = (5 < 4)
c = (4 < 10)

print(a, b, c)

# bool() function evaluates any value, and returns True or False

x = 'Hello'
y = 15

print(bool(x))
print(bool(y))

# some values do evaluate False as:
# empty values: (), [], {}, '', 0, None

# functions can return booleans:

def function():
    return True
print(function())

# isinstance()

x = 200
print(isinstance(x, int))
print(isinstance(x, float))
