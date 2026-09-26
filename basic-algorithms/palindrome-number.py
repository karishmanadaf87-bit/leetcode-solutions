class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original = x
        reversed_num = 0

        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        return original == reversed_num


# Test Case 1 - Typical case
print("Test Case 1:", Solution().isPalindrome(121))

# Test Case 2 - Edge case
print("Test Case 2:", Solution().isPalindrome(-121))