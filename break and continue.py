# break terminates a loop
# continue skips one iteration of a loop

manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

# skips an iteration when adding an item would exceed the limit
# breaks the loop if weight is exactly the value of the limit

weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking from the loop now!")
        break
    elif weight + cargo_weight > 100:
        print("  skipping {} ({})".format(cargo_name, cargo_weight))
        continue
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

# Adding strings until a certain number of characters is reached

headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
for headline in headlines:
    news_ticker += headline + ' '
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)

# check if number is prime

check_prime = [26, 39, 51, 53, 57, 79, 85, 2]

for n in check_prime:
    for i in range(2, n):
        if (n % i) == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(n, i, n))
            break
        if i == n - 1:
            print("{} IS a prime number".format(n))

def is_prime(n):
  for i in range(2, n):
    if (n%i) == 0:
      return False
  return True

print(is_prime(2))