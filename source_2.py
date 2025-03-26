# This is a simple and better way
dividers=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
symbols  = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
output=''
n = int(input())
for index,value in enumerate(dividers):
    while n>=value:
        output+=symbols[index]
        n-=value
print(output)

