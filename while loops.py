# while loops
## find the factorial of a number

number = 6
product = 1
current = 1

while number >= current:
    product *= current
    current += 1

print(product)

## while with step

start_num = int(input('Start number: '))
end_num = int(input('End number: '))
count_by = int(input('Count by: '))

if start_num > end_num:
    result = 'Oops! Looks like your start value is greater than the end value. Please try again.'

else:
    break_num = start_num
    while end_num > break_num:
        break_num += count_by

    result = break_num

print(result)

## nearest square

limit = int(input('Set limit: '))
nearest_square = 1
count = 1

while count**2 < limit:
    nearest_square = count **2
    count += 1

print(nearest_square)

## 