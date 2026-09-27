# Reverse Linked List

## Problem Name
Reverse Linked List

## Difficulty
Easy

## LeetCode
https://leetcode.com/problems/reverse-linked-list/

## Topic
Linked Lists

## Approach

The linked list is reversed using three pointers: `previous`, `current`, and `next_node`.

Initially, `previous` is set to `None` and `current` points to the head.

For each node, the next node is stored, the current node's link is reversed to point to the previous node, and the pointers are moved forward.

At the end, `previous` becomes the new head of the reversed linked list.

## Time Complexity

**O(n)**

Each node is visited once.

## Space Complexity

**O(1)**

Only a few pointer variables are used apart from the linked list.

## Test Cases

### Test Case 1 – Typical Case

**Input:**
```text
[1, 2, 3, 4, 5]