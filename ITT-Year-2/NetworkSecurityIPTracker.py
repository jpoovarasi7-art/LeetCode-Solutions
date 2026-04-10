first=set()
second=set()
third=set()
first_day=input("Enter the IP's address which is logged in successfully:")
second_day=input("Enter the IP's address which is failed logged attempts:")
third_day=input("Enter the IP's address which is blacklisted:")
word = ""
for char in first_day:
    if char == " " or char == "\n" or char == "\t":
        if word != "":
            first.add(word)
            word = ""
    else:
        word += char
if word != "":
    first.add(word)
word2 = ""
for char in second_day:
    if char == " " or char == "\n" or char == "\t":
        if word2 != "":
            second.add(word2)
            word2 = ""
    else:
        word2 += char
if word2 != "":
    second.add(word2)
word3 = ""
for char in third_day:
    if char == " " or char == "\n" or char == "\t":
        if word3 != "":
            third.add(word3)
            word3 = ""
    else:
        word3 += char
if word3 != "":
    third.add(word3)
found = False
while True:
   print("Menu driven")
   print("1.IP's that appear in both successful and failed logins but are not blacklisted.")
   print("2.IP's that attempted access but never succeeded.")
   print("3.IP's that are only blacklisted and never attempted login.")
   ch=int(input("Enter the choice:"))
   if ch==1:
      for i in first:
         if i in second and i not in third:
           print("IP's address in both success and failed but not in blacklisted:",i)
           found = True
      if not found:
         print("No one")
   elif ch==2:
      for i in second:
         if i not in first:
            print("IP's address attempted but not got success:",i)
            found = True
      if not found:
         print("NO one")
   elif ch==3:
       found = True
       for i in third:
          if i  not in second and i not in first:
              print("IP's address that are only blacklisted and never attempt to login:",i)
              found = False
       if  found:
          print("NO ONE")
   elif ch>4 or ch<1:
      print("Invalid choice,please Enter the choice")
   elif ch==4:
      break
