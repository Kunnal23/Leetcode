def reverseBits(n):
    reversed = 0
    for _ in range(32):
        reversed = (reversed << 1) | (n&1)
        n >>= 1 
    return reversed
    # binary = format(n & 0xFFFFFFFF, '032b') 
    # s = binary[::-1]
    # decimal = int(s, 2)
    # return decimal
    

print(reverseBits(100))