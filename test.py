numbers = [1,2,3,4,5]

even_numbers = []

#-------------------1
# for number in numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)

# print("Even numbers:", even_numbers) 

#-------------------2
# def is_even(number):
#     return number % 2 == 0
# even_numbers = list(filter(is_even, numbers))
# print("Even numbers:", even_numbers)

#-------------------3
# even_numbers = filter(lambda x: x % 2 == 0, numbers)
# print("Even numbers:", list(even_numbers))

#-------------------4 map + lambda
# prices = [100, 200, 500, 900, 50000]
# price_increase = list(map(lambda x: x * 1.1 if x >= 500 else x*0.9, prices))
# print("Prices after increase:", price_increase)

#-------------------5 list comprehension
# prices = [100, 200, 500, 900, 50000]
# price_increase = [x * 1.1 if x >= 500 else x*0.9 for x in prices]
# print(price_increase)

#-------------------6 vanlig loop
prices = [100, 200, 500, 900, 50000]
price_increase = []
for x in prices:
    if x >= 500:
        price_increase.append(x * 1.1)  # öka priset
    else:
        price_increase.append(x * 0.9)        # behåll som det är

print(price_increase)
