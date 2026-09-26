# Palindrome Number

## Problem Name
Palindrome Number

## Difficulty
Easy

## LeetCode
https://leetcode.com/problems/palindrome-number/

## Approach

The solution checks whether the given integer reads the same forward and backward.

Negative numbers are immediately considered not palindromes. For a positive number, the digits are reversed using the modulo (`%`) and integer division (`//`) operations. The reversed number is then compared with the original number.

## Time Complexity

**O(log n)**

The number of digits in the number is processed once.

## Space Complexity

**O(1)**

Only a few variables are used.

## Test Cases

### Test Case 1 – Typical Case

**Input:**
```text
x = 121