class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }

        s = s.replace('IV', 'IIII').replace('IX', 'VIIII')
        s = s.replace('XL', 'XXXX').replace('XC', 'LXXXX')
        s = s.replace('CD', 'CCCC').replace('CM', 'DCCCC')

        total = 0

        for i in range(len(s)):
            total += roman_map[s[i]]

        return total


# Test Case 1 - Typical case
print("Test Case 1:", Solution().romanToInt("III"))

# Test Case 2 - Edge case
print("Test Case 2:", Solution().romanToInt("MCMXCIV"))