max =5
total = 0.0

print('This program calculate the sum of')
print(max,'numbers you will enter')
for count in range(max):
    number = int(input('Enter a number: '))
    total = total + number
print('the total is',total)