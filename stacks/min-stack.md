# Min Stack

## Problem Name
Min Stack

## Difficulty
Medium

## LeetCode
https://leetcode.com/problems/min-stack/

## Topic
Stacks

## Approach

Two stacks are used.

The first stack stores all the values.

The second stack, called `min_stack`, stores the minimum values. Whenever a new value is pushed, it is added to `min_stack` if it is smaller than or equal to the current minimum.

When the minimum value is removed from the main stack, it is also removed from `min_stack`.

This allows the minimum value to be retrieved in constant time.

## Time Complexity

- `push()` → O(1)
- `pop()` → O(1)
- `top()` → O(1)
- `getMin()` → O(1)

## Space Complexity

**O(n)**

Two stacks are used to store the elements.

## Test Cases

### Test Case 1 – Typical Case

Operations:

```text
push(-2)
push(0)
push(-3)
getMin()
pop()
top()