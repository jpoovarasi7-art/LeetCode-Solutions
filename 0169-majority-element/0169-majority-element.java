class Solution {
    public int majorityElement(int[] nums) {
        int count = 0;
        int can=0;
        for(int i:nums)
        {
            if(count==0)
            {
                can=i;
            }
            if(can==i)
            {
                count++;
            }
            else{count--;}
        }
        return can;
    }
    public static void main(String[] args)
    {
        Solution solver = new  Solution();
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] num = new int[n];
        for(int i=0;i<n;i++)
        {
            num[i] = scan.nextInt();
        }
        int ans = solver.majorityElement(num);
        System.out.println(ans);
    }
}