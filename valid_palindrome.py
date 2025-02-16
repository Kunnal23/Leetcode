def isPalindrome(s):
    # Brute Force
    # s = "".join(char.lower() for char in s if char.isalnum())
    # return s == s[::-1]

    s = "".join(char.lower() for char in s if char.isalnum())
    n = len(s)
    mid = n//2
    for i in range(mid):
        if s[i] != s[n-i-1]:
            return False
    return True