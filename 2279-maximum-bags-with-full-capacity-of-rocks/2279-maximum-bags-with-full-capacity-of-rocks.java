import java.util.Arrays;

class Solution {
    public int maximumBags(int[] capacity, int[] rocks, int additionalRocks) {
        int n = capacity.length;
        int[] vacancies = new int[n];
        for (int i = 0; i < n; i++) {
            vacancies[i] = capacity[i] - rocks[i];
        }
        Arrays.sort(vacancies);
        int fullBags = 0;
        for (int i = 0; i < n; i++) {
            if (additionalRocks >= vacancies[i]) {
                additionalRocks -= vacancies[i];
                fullBags++;
            } else {
                break;
            }
        }   
        return fullBags;
    }
}
