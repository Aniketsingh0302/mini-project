import string

def reverse(message):
     return message[::-1]
choice = int(input("Enter 1 to code or 2 to decode \n"))
coded =""
if choice == 1:
    msg = input("enter your message: \n")
    if len(msg) <=3:
        coded = reverse(msg)
    else:
         replaced_code =  msg.replace("a","@#",50)
         coded =reverse(replaced_code)

    print(coded)

elif choice == 2:
     coded=input("enter your message:")
     if len(coded) <=3:
          print(reverse(coded))
     else:
         replace_code = coded.replace("#@","a",50)
         decode = reverse(replace_code)
         print(decode)
else:
     print("Exiting...") #gfhjgjhgjef
