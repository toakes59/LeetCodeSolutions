# Palindrome_number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_num = 0
        temp = x

        while temp > 0:
            reversed_num = reversed_num * 10 + temp % 10
            temp //= 10

        return x == reversed_num