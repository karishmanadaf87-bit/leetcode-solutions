# Roman to Integer

--Problem Name
Roman to Integer

-- Difficulty
Easy

## LeetCode
https://leetcode.com/problems/roman-to-integer/

## Approach

The solution uses a mapping of Roman numeral characters to their integer values.

First, the special subtractive combinations such as IV, IX, XL, XC, CD, and CM are replaced with their equivalent repeated-value forms.

Then, each Roman numeral character is converted using the map and added to the total.

## Time Complexity

**O(n)**

The string is processed using replacement operations and a loop through the characters.

## Space Complexity

**O(n)**

The string may be modified during the replacement operations.

## Test Cases

### Test Case 1 – Typical Case

**Input:**
3
s = "III"