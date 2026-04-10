first=set()
second=set()
first_day=input("Enter the student ROLLNO. are present in first day:")
second_day=input("Enter the student ROLLNO. are present in second day:")
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
found = False
while True:
   print("Menu driven")
   print("1.Identify students present on both days.")
   print("2.Identify students present on either days.")
   print("3.Identify students absent on second days.")
   ch=int(input("Enter the choice:"))
   if ch==1:
      for i in first:
         if i in second:
           print("Student present on both days:",i)
           found = True
      if not found:
         print("No one")
   elif ch==2:
      unions=set()
      unions=first.copy()
      for i in second:
         if i not in first:
           unions.add(i)
           found = True
      if not found:
         print("NO one")
         break
      print("Student present on either days:",unions)
   elif ch==3:
       for i in first:
          if i not in second:
           print("Student who are absent on second day:",i)
           found = True
       if not found:
          print("NO ONE")
   elif ch>4 or ch<1:
      print("Invalid choice,please Enter the choice")
   elif ch==4:
      break
