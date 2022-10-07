# functions


def my_function():
    print('Hi')

my_function()


def my_function(name):                              # parameter or argument
    print(name + ' Surname')


my_function('Tom')


def my_function(*kids):
    print('The youngest child is ' + kids[2])       # if the number of arguments is not defined, * and list

my_function('Emil', 'Mark', 'Linus')


def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus
