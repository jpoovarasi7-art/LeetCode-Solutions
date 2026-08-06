#include <stdio.h>
#include <stdlib.h>

// Keep this helper function
int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

// Keep the core engine function
int subarrayBitwiseORs(int* arr, int arrSize) {
    if (arrSize == 0) return 0;

    int max_possible_elements = arrSize * 31;
    int* total_results = (int*)malloc(max_possible_elements * sizeof(int));
    
    int total_count = 0; 
    int current_start = 0; 
    int current_end = 0;   

    for (int i = 0; i < arrSize; i++) {
        int next_end = total_count;
        total_results[total_count++] = arr[i];
        
        for (int j = current_start; j < current_end; j++) {
            int new_or_val = total_results[j] | arr[i];
            if (new_or_val != total_results[total_count - 1]) {
                total_results[total_count++] = new_or_val;
            }
        }
        
        qsort(&total_results[next_end], total_count - next_end, sizeof(int), compare);
        
        int unique_idx = next_end;
        for (int j = next_end + 1; j < total_count; j++) {
            if (total_results[j] != total_results[unique_idx]) {
                unique_idx++;
                total_results[unique_idx] = total_results[j];
            }
        }
        total_count = unique_idx + 1;
        
        current_start = next_end;
        current_end = total_count;
    }

    qsort(total_results, total_count, sizeof(int), compare);
    
    int distinct_count = (total_count > 0) ? 1 : 0;
    for (int i = 1; i < total_count; i++) {
        if (total_results[i] != total_results[i - 1]) {
            distinct_count++;
        }
    }

    free(total_results);
    return distinct_count;
}
// DO NOT ADD ANY CODE BELOW THIS LINE
