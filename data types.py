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