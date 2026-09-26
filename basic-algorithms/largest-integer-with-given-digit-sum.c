#include <stdio.h>

int largestInteger(int n, int s)
{
    if (s == 0)
        return 0;

    if (s > 9 * n)
        return -1;

    int ans = 0;

    while (n--) {
        if (s >= 9) {
            ans = ans * 10 + 9;
            s -= 9;
        } else {
            ans = ans * 10 + s;
            s = 0;
        }
    }

    return ans;
}

int main()
{
    // Test Case 1 - Typical case
    printf("Test Case 1: %d\n", largestInteger(2, 15));

    // Test Case 2 - Edge case
    printf("Test Case 2: %d\n", largestInteger(2, 20));

    return 0;
}