# data types

x = str('Hello World')
print(type(x))

x = int(20)
print(type(x))

x = float(20.5)
print(type(x))

x = complex(1j)
print(type(x))

x = list(("apple", "banana", "cherry"))	      # list [] can be modified
print(type(x))

x = tuple(("apple", "banana", "cherry"))        # tuple () can´t be modified
print(type(x))

x = range(6)
print(type(x))

x = {"name" : "John", "age" : 36}             # dict {}
print(type(x))

x = {"apple", "banana", "cherry"}             # set
print(type(x))

x = frozenset({"apple", "banana", "cherry"})   # frozenset
print(type(x))

x = bool(5)
print(type(x))

x = b"Hello"
print(type(x))

x = bytearray(5)
print(type(x))

x = memoryview(bytes(5))
print(type(x))

x = None
print(type(x))

# type conversion

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# casting: specify a type on a variable

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
