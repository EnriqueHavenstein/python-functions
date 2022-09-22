# for loops
## cities [list] broken down using a for loop

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city)

## range() built in function used to create an iterable sequence of numbers

for i in range(3):
    print("Hi!")

## range(start=0, stop, step=1)

for i in range(2, 10, 2):
    print(i)

# creating a new list

## .append() used to add items to the end (first free space) of a given list
## .title() returns a string where the first character in every word is upper case

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())

print(capitalized_cities)

## .lower() method takes no arguments and returns a string converting each uppercase character to lowercase
## .replace() method replaces a specified phrase with another specified phrase

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

for name in names:
    usernames.append(name.lower().replace(' ', '_'))

print(usernames)

# modifying a list
# len() returns the number of items in an object

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for index in range(len(cities)):
    cities[index] = cities[index].title()

print(cities)

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for index in range(len(usernames)):
    usernames[index] = usernames[index].lower().replace(' ', '_')

print(usernames)

# iterating over a list and verifying a condition (HTML starts with < and ends with >)
## .count() returns the number of elements with the specified value

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1

print(count)

# creating a HTML str
# "\ n" is the character that marks the end of the line,
                     # it does the characters that are after it in html_str
                     # are on the next line

items = ['first string', 'second string']
html_str = "<ul>\n"

for item in items:
    html_str += "<li>{}</li>\n".format(item)

html_str = html_str + "</ul>"

print(html_str)

# find the factorial of a number with for loop

number = 6
product = 1

for i in range(2, number + 1):
    product *= i

print(product)