test=int(input("Enter the number of test cases:"))
for i in range(test):
   first=int(input("Enter the charges for FIRST service delivery:"))
   second=int(input("Enter the charges for SECOND srvice delivery:"))
   if first>second:
      print("FIRST")
   elif first==second:
      print("ANY")
   else:
      print("SECOND")
