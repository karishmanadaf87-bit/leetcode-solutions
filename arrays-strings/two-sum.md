# Two Sum

## Problem Name

Two Sum

## Difficulty

Easy

## LeetCode

https://leetcode.com/problems/two-sum/

## Approach

The solution uses a brute-force approach.

We check every possible pair of elements in the array. For each pair, we add the two numbers and compare their sum with the target.

If the sum equals the target, we return the indices of those two numbers.

## Time Complexity

**O(n²)**

Two nested loops are used to check pairs of elements.

## Space Complexity

**O(1)**

No extra data structure is used apart from the variables required for the loops.

## Test Cases

### Test Case 1 – Typical Case

**Input:**

```text
nums = [2, 7, 11, 15]
target = 9
```

**Output:**

```text
[0, 1]
```

### Test Case 2 – Edge Case

**Input:**

```text
nums = [3, 3]
target = 6
```

**Output:**

```text
[0, 1]
```

## Notes / Edge Cases

* The same element cannot be used twice.
* Two different elements can have the same value.
* The solution returns the indices of the two numbers.
* The solution was tested locally in VS Code before submission to LeetCode.
