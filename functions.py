# functions


def my_function():
    print('Hi')


my_function()


def my_function(name):                              # parameter or argument
    print(name + ' Surname')


my_function('Tom')


def my_function(*kids):                             # arbitrary arguments
    print('The youngest child is ' + kids[2])       # if the number of arguments is not defined, * and receive tuple


my_function('Emil', 'Mark', 'Linus')


def my_function(child3, child2, child1):            # keyword arguments
    print("The youngest child is " + child3)        # This way the order of the argument does not matter


my_function(child1="Emil", child2="Tobias", child3="Linus")


def my_function(**kid):                             # arbitrary keyword arguments
    print("His last name is " + kid["lname"])       # when the number of arguments is unknown


my_function(fname="Tobias", lname="Refsnes")


def my_function(country="Norway"):                  # default parameter value
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()                                       # when calling the function without argument prints default value
my_function("Brazil")


def my_function(food):                              # list as an argument
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)


def my_function(x):                                 # return statement
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))


def tri_recursion(k):                               # recursion: a function can call itself
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)
