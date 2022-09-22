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

## add the first 5 odd numbers in a list

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
count_odd = 0
list_sum = 0
len_num_list = len(num_list)
i = 0

while (count_odd < 5) and (i < len_num_list):
    if num_list[i] % 2 > 0:
        count_odd += 1
        list_sum += num_list[i]
    i += 1

print('The numbers of odd numbers added are: {}'.format(count_odd))
print('The sum of the odd numbers added is: {}'.format(list_sum))