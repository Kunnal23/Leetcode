# def calc(self, num):
#     temp = num
#     curr = 0
#     while temp > 0:
#         digit = temp % 10
#         curr += digit
#         temp //= 10
#     return curr
def addDigits(num):
#     while (num // 10) != 0:
#         num = self.calc(num)
#     return num
    if num == 0:
        return 0
    return 1 + (num - 1) % 9

print(addDigits(191))