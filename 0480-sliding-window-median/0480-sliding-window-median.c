#include <stdlib.h>

static int cmp(const void *a, const void *b) {
    int x = *(const int *)a, y = *(const int *)b;
    return (x > y) - (x < y);
}

static int m;
static int *bit;
static int *u;

static void add(int i, int d) {
    for (; i <= m; i += i & -i) bit[i] += d;
}

static int kth(int k, int top) {
    int pos = 0;
    for (int pw = top; pw > 0; pw >>= 1) {
        if (pos + pw <= m && bit[pos + pw] < k) {
            pos += pw;
            k -= bit[pos];
        }
    }
    return u[pos];
}

double* medianSlidingWindow(int* nums, int numsSize, int k, int* returnSize) {
    int n = numsSize;
    *returnSize = n - k + 1;
    double *res = (double *)malloc(sizeof(double) * (*returnSize));

    int *s = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++) s[i] = nums[i];
    qsort(s, n, sizeof(int), cmp);

    u = (int *)malloc(sizeof(int) * n);
    m = 0;
    for (int i = 0; i < n; i++) {
        if (i == 0 || s[i] != s[i - 1]) u[m++] = s[i];
    }
    free(s);

    int *rank = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++) {
        int lo = 0, hi = m - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (u[mid] < nums[i]) lo = mid + 1;
            else hi = mid;
        }
        rank[i] = lo + 1;
    }

    bit = (int *)calloc(m + 1, sizeof(int));
    int top = 1;
    while (top * 2 <= m) top *= 2;

    for (int i = 0; i < k; i++) add(rank[i], 1);

    for (int i = 0; ; i++) {
        if (k % 2 == 1) {
            res[i] = (double)kth(k / 2 + 1, top);
        } else {
            double a = (double)kth(k / 2, top);
            double b = (double)kth(k / 2 + 1, top);
            res[i] = (a + b) / 2.0;
        }
        if (i + k >= n) break;
        add(rank[i], -1);
        add(rank[i + k], 1);
    }

    free(rank);
    free(bit);
    free(u);
    return res;
}