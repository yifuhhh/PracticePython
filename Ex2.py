a = int(input("Give me a number: "))
if a % 2 == 0:
    if a % 4 == 0:
        print ("It's a multiple of 4.")
    else:
        print ("It's an even num.")
else:
    print ("It's an odd num.")

num = int(input("Give me a number again: "))
check = int(input("OK give me another number: "))
if check % num == 0:
    print (str(check) + "could be divided into " + str(num))
else:
    print ("Fuck off")
