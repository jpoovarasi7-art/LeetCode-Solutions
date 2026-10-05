#include <stdio.h>
#include <stdlib.h>

int* maxSlidingWindow(int* nums, int numsSize, int k, int* returnSize)
{
    int *result;
    int *deque;
    int front = 0;
    int rear = 0;
    int i;
    int resultIndex = 0;

    *returnSize = numsSize - k + 1;

    result = (int *)malloc((*returnSize) * sizeof(int));
    deque = (int *)malloc(numsSize * sizeof(int));

    for (i = 0; i < numsSize; i++)
    {
        /* Remove elements outside the window */
        while (front < rear && deque[front] <= i - k)
        {
            front++;
        }

        /* Remove smaller elements */
        while (front < rear &&
               nums[deque[rear - 1]] <= nums[i])
        {
            rear--;
        }

        deque[rear] = i;
        rear++;

        /* Store maximum of current window */
        if (i >= k - 1)
        {
            result[resultIndex] = nums[deque[front]];
            resultIndex++;
        }
    }

    free(deque);

    return result;
}