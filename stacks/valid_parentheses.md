# Valid Parentheses

## Problem Name
Valid Parentheses

## Difficulty
Easy

## LeetCode
https://leetcode.com/problems/valid-parentheses/

## Topic
Stacks

## Approach

A stack is used to keep track of opening brackets.

When an opening bracket `(`, `{`, or `[` is found, it is pushed onto the stack.

When a closing bracket is found, the top opening bracket is removed and checked to make sure it matches the closing bracket.

At the end, the stack must be empty for the string to be valid.

## Time Complexity

**O(n)**

Each character is processed once.

## Space Complexity

**O(n)**

The stack can contain up to `n` opening brackets.

## Test Cases

### Test Case 1 – Typical Case

**Input:**
```text
()[]{}