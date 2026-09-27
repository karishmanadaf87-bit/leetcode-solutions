# Merge Two Sorted Lists

## Problem Name
Merge Two Sorted Lists

## Difficulty
Easy

## LeetCode
https://leetcode.com/problems/merge-two-sorted-lists/

## Topic
Linked Lists

## Approach

Two sorted linked lists are merged by comparing the current nodes of both lists.

A dummy node is used to simplify the process. The smaller node is attached to the merged list, and the corresponding pointer is moved forward.

When one list becomes empty, the remaining nodes of the other list are attached to the merged list.

## Time Complexity

**O(n + m)**

Each node from both linked lists is visited once.

## Space Complexity

**O(1)**

Only pointer variables are used. No new list of nodes is created.

## Test Cases

### Test Case 1 – Typical Case

**Input:**

```text
list1 = [1, 2, 4]
list2 = [1, 3, 4]