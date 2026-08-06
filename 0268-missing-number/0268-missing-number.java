class Solution {
    public int missingNumber(int[] nums) {
        int n =nums.length;
        boolean[] seen = new boolean[n+1];
        for(int i:nums)
        {
            seen[i] = true;
        }
        for(int i=0;i<=n;i++)
        {
            if(!seen[i])
            {
                return i;
            }
        }
        return -1;
    }
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] num = new int[n];
        for(int i=0;i<n;i++)
        {
            num[i]=scan.nextInt();
        }
        Solution solver = new Solution();
        System.out.println();
    }
}