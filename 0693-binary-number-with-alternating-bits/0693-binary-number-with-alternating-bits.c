bool hasAlternatingBits(int n) {
    int j=0,i=0;
    int stared = 0;
    char data[50];
    if(n==0) return true;
   for(i=31;i>=0;i--) 
   {
    int current = (n>>i) & 1;
    if(current == 1){ stared = 1;}
    if(stared){ 
    data[j]=current + '0';
    j++;
    }
   }
   data[j]='\0';
   for(i=0;i<strlen(data) && data[i]!='\0';i++)
   {
    if(data[i]=='1')
    {
        if(data[i+1]=='1')
        {
            return false;
        }
    }
    if(data[i]=='0')
    {
        if(data[i+1]=='0')
        {
            return false;
        }
    }
   }
    return true;
}