class Solution {
    public String countAndSay(int n) {
        if (n <= 0) return "";
        
        String result = "1";

        // Iteratively build the sequence from 1 up to n
        for (int i = 1; i < n; i++) {
            StringBuilder current = new StringBuilder();
            int count = 1;

            // Perform Run-Length Encoding on the result from the previous iteration
            for (int j = 0; j < result.length(); j++) {
                // If the next character is the same, increment count
                if (j + 1 < result.length() && result.charAt(j) == result.charAt(j + 1)) {
                    count++;
                } else {
                    // Append count followed by the digit character
                    current.append(count).append(result.charAt(j));
                    count = 1; // Reset count for the next sequence
                }
            }

            result = current.toString();
        }

        return result;
    }
}