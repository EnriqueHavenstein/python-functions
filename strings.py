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
print(a.strip())                 # returns 'I have done this'

# replace() method replaces a string with another string

a = 'Hello, World'
print(a.replace('l', ' '))

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
item_no = 567
price = 49.95
my_order = "I want {} pieces of item {} for {} dollars."     # "I want {2} pieces of item {0} for {1} dollars."
print(my_order.format(quantity, item_no, price))              # can be done to avoid confusion

# escape characters

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

#   \'	    # Single Quote
#   \\	    # Backslash
#   \n	    # New Line
#   \r	    # Carriage Return
#   \t	    # Tab
#   \b      # Backspace
#   \f	    # Form Feed
#   \ooo	# Octal value
#   \xhh	# Hex value

# capitalize()  	Converts the first character to upper case
# casefold()	    Converts string into lower case
# center()   	    Returns a centered string
# count()	        Returns the number of times a specified value occurs in a string
# encode()	        Returns an encoded version of the string
# endswith()	    Returns true if the string ends with the specified value
# expandtabs()	    Sets the tab size of the string
# find()    	    Searches the string for a specified value and returns the position of where it was found
# format()  	    Formats specified values in a string
# format_map()	    Formats specified values in a string
# index()   	    Searches the string for a specified value and returns the position of where it was found
# isalnum()  	    Returns True if all characters in the string are alphanumeric
# isalpha() 	    Returns True if all characters in the string are in the alphabet
# isdecimal()	    Returns True if all characters in the string are decimals
# isdigit() 	    Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()     	Returns True if all characters in the string are lower case
# isnumeric()   	Returns True if all characters in the string are numeric
# isprintable() 	Returns True if all characters in the string are printable
# isspace()     	Returns True if all characters in the string are whitespaces
# istitle()     	Returns True if the string follows the rules of a title
# isupper()     	Returns True if all characters in the string are upper case
# join()        	Joins the elements of an iterable to the end of the string
# ljust()       	Returns a left justified version of the string
# lower()       	Converts a string into lower case
# lstrip()      	Returns a left trim version of the string
# maketrans()   	Returns a translation table to be used in translations
# partition()    	Returns a tuple where the string is parted into three parts
# replace()     	Returns a string where a specified value is replaced with a specified value
# rfind()       	Searches the string for a specified value and returns the last position of where it was found
# rindex()      	Searches the string for a specified value and returns the last position of where it was found
# rjust()       	Returns a right justified version of the string
# rpartition()  	Returns a tuple where the string is parted into three parts
# rsplit()      	Splits the string at the specified separator, and returns a list
# rstrip()      	Returns a right trim version of the string
# split()       	Splits the string at the specified separator, and returns a list
# splitlines()  	Splits the string at line breaks and returns a list
# startswith()	    Returns true if the string starts with the specified value
# strip()	        Returns a trimmed version of the string
# swapcase()    	Swaps cases, lower case becomes upper case and vice versa
# title()       	Converts the first character of each word to upper case
# translate()   	Returns a translated string
# upper()       	Converts a string into upper case
# zfill()       	Fills the string with a specified number of 0 values at the beginning

x = 'Hello'
print(len(x))


