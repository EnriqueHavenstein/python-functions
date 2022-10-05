# Python Collections (Arrays)

#   There are four collection data types in the Python programming language:
#       List is a collection which is ordered and changeable. Allows duplicate members. []
#       Tuple is a collection which is ordered and unchangeable. Allows duplicate members. ()
#       Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#       Dictionary is a collection which is ordered** and changeable. No duplicate members. {}

list_1 = ['apple', 'banana', 'cherry']              # indexed. 0, 1, 2 ...
print(list_1)

list_1 = ["abc", 34, True, 40, "male", "male"]      # lists can contain different data types
print(list_1)

print(len(list_1))
print(type(list_1))                                 # <class 'list'>

list_1 = list(('apple', 'banana', 'orange'))
print(list_1)

# access items

print(list_1[0])        # returns first item
print(list_1[-1])       # returns last item
print(list_1[2:4])      # returns third and fourth item
print(list_1[:4])       # from the beginning to third position
print(list_1[2:])       # from the third position to the end

list_1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list_1[-4:-1])    # from 'orange' (-4) to, but not including 'mango' (-1)

if "apple" in list_1:
    print("Yes, 'apple' is in the fruits list")

# change list items

list_1[1] = 'orange'
list_1[1:3] = ['watermelon', 'peach']

# If you insert more or less items than you replace, the new items will be inserted where you specified
# and the remaining items will move accordingly:

print(len(list_1))
list_1[1:2] = ['banana', 'watermelon']
print(list_1)
print(len(list_1))

# insert items

list_1 = ['apple', 'banana', 'cherry']
list_1.insert(2, 'watermelon')
print(list_1)

# add list items

list_1 = ['apple', 'banana', 'orange']
list_1.append('watermelon')
print(list_1)

# extend list

list_1 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
list_1.extend(tropical)
print(list_1)

# remove list items

list_1 = ["apple", "banana", "cherry"]
list_1.remove("banana")                         # .remove() method
print(list_1)

# remove specified index

list_1 = ["apple", "banana", "cherry"]
list_1.pop(1)                                   # .pop() method, when used without argument removes last item
print(list_1)
del list_1[0]
print(list_1)
list_1.clear()                                  # .clear() the list still exist but has no items
print(list_1)

# copy a list: don't do list_1 = list_2

list_1 = ["apple", "banana", "cherry"]
list_2 = list_1.copy()
print(list_2)

# join lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list_1 = ["a", "b" , "c"]
list_2 = [1, 2, 3]

for x in list_2:
  list_1.append(x)

print(list_1)
