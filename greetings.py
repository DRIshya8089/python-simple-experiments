import time

hour = int(time.strftime('%H'))
print("now the time is : ", time.strftime('%H:%M'))
if (hour>= 0) and (hour<12) :
    print("Good Morning Sir")
elif (hour>= 12) and (hour <4):
    print("Good Afternoon Sir")
elif (hour>= 4) and (hour <7) :
    print("Good Evening Sir")
elif (hour>= 7) and (hour <0) :
    print("Good Night Sir")