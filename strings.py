# multiline strings

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

print(a)

# strings are arrays

a = "Hello, World!"
print(a[1])

for letter in 'banana':
    print(letter)

# length of a string: len()

x = 'Hello'
print(len(x))

# check string

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# check if not

txt = "The best things in life are free!"
print("expensive" not in txt)

# slicing strings

b = "Hello, World!"
print(b[2:5])           # get the characters from position 2 to position 5 (not included)
print(b[:5])            # slice from the start
print(b[2:])            # slice to the end

# negative indexing

b = 'Hello, World!'
print(b[-5:-2])         # from 'o' in World to 'd' in World but not included

# upper() method returns the string in upper case

b = 'Hello, World!'
print(b.upper())

# lower() method returns the string in lower case

b = 'Hello, World!'
print(b.lower())

# strip() method removes any whitespace from the beginning or the end

a = '    I have done this      '
print(a.strip())

# replace() method replaces a string with another string

a = 'Hello, World'
print(a.replace('l',' '))

# split() method splits the string into substrings if it finds instances of the separator

a = "Hello, World!"
print(a.split(","))     # returns ['Hello', ' World!']

# string concatenation

a = 'Hi'
b = 'John'
c = a + ' ' + b
print(c)

# format() method to insert numbers into strings

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."     # "I want {2} pieces of item {0} for {1} dollars."
print(myorder.format(quantity, itemno, price))              # can be done to avoid confusion

