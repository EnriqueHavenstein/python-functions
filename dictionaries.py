# dictionaries

# Method 1: Using a for loop to create a set of counters

## list containing book titles
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']

## creation of empty dictionary
word_counter = {}

## for each position in book title,
## if the word is not in the dictionary, sets value to 1.
## Else (it is already) increases count by 1.
for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1

print(word_counter)

# Method 2: Using the get method

book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}

## dictionary.get(keyname, value)
## returns the value for the given key if present in the dictionary.
## If not, then it will return None (if get() is used with only one argument).

for word in book_title:
    word_counter[word] = word_counter.get(word, 0) + 1

print(word_counter)

## keys and values in a dictionary

cast = {
    "Jerry Seinfeld": "Jerry Seinfeld",
    "Julia Louis-Dreyfus": "Elaine Benes",
    "Jason Alexander": "George Costanza",
    "Michael Richards": "Cosmo Kramer"
}

print("Iterating through keys:")
for key in cast:
    print(key)

## dictionary.items() returns a list of dictionary's (key, value) tuple pairs

print("\nIterating through keys and values:")
for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))

# You would like to count the number of fruits in your basket.
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
#if the key is in the list of fruits, add the value (number of fruits) to result

for object, count in basket_items.items():
    if object in fruits:
        result += count

print(result)

# You would like to count the number of fruits in your basket.
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Iterate through the dictionary
for object, count in basket_items.items():
    if object in fruits:
        fruit_count += count
    else:
        not_fruit_count += count

print(fruit_count, not_fruit_count)