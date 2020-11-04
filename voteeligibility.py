ans = True
while ans:
    ans = int(input("ENTER YOUR AGE = "))
    if ans >=18 :
        print("YOU ARE ELIGIBLE TO VOTE")
    elif ans < 18 :
        print("YOU ARE NOT ELIGIBLE TO VOTE")
    a = input("DO YOU WANT TO TRY AGAIN ? (Y/N) = ")
    if a == "Y" : 
        input("PRESS ENTER TO CONTINUE")
    if a == "N" :
        break
