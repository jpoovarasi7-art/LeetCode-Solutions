while True:
   print("*"*10,"Email and password verfication","*"*10)
   email=input("Enter Email:")
   index=email.find("@")
   half_email = email.split("@")[0]
   for i in half_email:
          if i==".":
               print("Enter the valid Email-ID")
               break
          elif (97<=ord(i)<=122 or int(i)<=9 and int(i)>=0):
               continue
          else:
               break
   remaining_string  = email[index:]
   if remaining_string=="@gmail.com":
     print("Your Email is a valid one")
     break
   elif remaining_string=="@mepcoeng.ac.in":
     print("Your Email is a valid one")
     break
   else:
     print("Please,Enter valid one")
password=input("Enter password:")
if len(password)<8:
   print("Least we have 8 character")
else:
   s1=('!','@','#','$','%','^','&','*','()')
   s2=('0','1','2','3','4','5','6','7','8','9')
   u=d=x=a=t=0
   for i in password:
      if 97<=ord(i)<=122:
         u=1
      elif 65<=ord(i)<=90:
         d=1
      elif i in s2:
         a=1
      elif i=="":
         t=1
      elif i in s1:
         x=1
   if u==1 and d!=1 and a!=1 and x!=1 and t!=1:
      print("Password must contains alteast one uppercase character, one special character and one digit, it might have a space")
   elif u!=1 and d==1 and a!=1 and x!=1 and t!=1:
      print("Password must contains alteast one lowercase character, one special character and one digit, it might have a space")
   elif u!=1 and d!=1 and a==1 and x!=1 and t!=1:
      print("Password must contains alteast one lowercase character, one uppercase character and one special character, it might have a space")
   elif u!=1 and d!=1 and a!=1 and x==1 and t!=1:
      print("Password must contains alteast one lowercase character, one uppercase character and one digit, it might have a space")
   else:
      print("The password validation is done")
print("*"*52);
