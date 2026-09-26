# Largest Integer With Given Digit Sum

## Problem Name
Largest Integer With Given Digit Sum

## Difficulty
Easy

## LeetCode
https://leetcode.com/problems/largest-number-with-given-sum/

## Approach

The solution constructs the largest possible number with exactly `n` digits whose digits add up to `s`.

Since we want the largest number, we place the largest possible digit, `9`, at each position first. If the remaining sum is less than `9`, that remaining value is placed in the next position.

If the required sum is greater than `9 * n`, it is impossible to create such a number, so the solution returns `-1`.

## Time Complexity

**O(n)**

The algorithm processes each digit position once.

## Space Complexity

**O(1)**

Only a few integer variables are used.

## Test Cases

### Test Case 1 – Typical Case

**Input:**
```text
n = 2
s = 15