class Solution {
    public boolean hasMatch(String s, String p) {
        int index = p.indexOf("*");
        String sub1 = p.substring(0,index);
        String sub2 = p.substring(index+1);
        int first = s.indexOf(sub1);
        if(first==-1)
        {
            return false;
        }
        int second = s.indexOf(sub2,first+sub1.length());
        if(second==-1)
        {
            return false;
        }
        return true;
    }
}