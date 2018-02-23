#  comparison operators
#  decision making
#  if else..works for one condition
#  elif is for multiple condition
marks = 78

if marks < 50:
    print("You Failed!")
    print("YOU REPEAT CLASS")

elif marks >=50 and marks < 60:
    print("YOU GOT AN AVERAGE")

elif marks >=60 and marks < 70:
     print("YOU GOT ABOVE AVERAGE")

elif marks >=70 and marks < 100:
    print("Excellent!")

else:
    print("INVALID!")
    print("PLEASE RE-ENTER")

#  Prompt for year, check if its leap or not

#  pseudo code
#  enter year
# check is divisible by 4


year = 2004

if year%4 ==0:
    if year%100!=0:
        if year%400==0:
            print("ITS A LEAP YEAR")
        else:
            print("Its not a leap year1")
    else:
        print("Its a leap year")
else:
    print("Not a leap year3")


print("---WHILE----")
count = 0 #initialize loop
while count < 100:# condition
    print("hello kenya", count)
    #increament
    count = count+1


# Create a multiplication complete
x = 0
y = 0
while x < 10:
    print(y, " * ",x)
    x = x + 1
    while y < 10:
        print("OK")






















































