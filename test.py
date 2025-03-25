
num = 36**8 + 6**20 - 12
a = num
result = ""
while a >= 1:
    number = a - 6 * (a // 6)
    result += str(number)
    a = a // 6

print(result[::-1])