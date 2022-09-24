# list comprehension

# previously creating a list and iterating with for

cities = ['new york', 'berlin', 'madrid', 'los angeles', 'rome', 'paris']
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())

print (capitalized_cities)

# the previous method can be replaced and reduced to:

cities = ['new york', 'berlin', 'madrid', 'los angeles', 'rome', 'paris']
capitalized_cities = [city.title() for city in cities]

print (capitalized_cities)

# conditionals in list comprehension

squares = [x**2 for x in range(9) if x % 2 == 0]
print(squares)

squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
print(squares)

# extract first names

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names]
print(first_names)

# multiples of 3

multiples_3 = [x for x in range(30) if x % 3 == 0]
print(multiples_3)

# filter names by scores

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name, score in scores.items() if score >= 65]
print(passed)
