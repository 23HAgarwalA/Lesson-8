speed1 = int(input("Enter your first speed: "))
speed2 = int(input("Enter your second speed: "))
speed3 = int(input("Enter your third speed: "))
averagespeed = (speed1+speed2+speed3)/3
print ("The average speed is ", averagespeed)
if speed1<averagespeed:
    print ("Speed 1 is slower than the average by ", averagespeed-speed1)
else:
    print ("Speed 1 is faster than the average speed by", speed1-averagespeed)
if speed2<averagespeed:
    print ("Speed 2 is slower than the average by ", averagespeed-speed2)
else:
    print ("Speed 2 is faster than the average speed by", speed2-averagespeed)
if speed3<averagespeed:
    print ("Speed 3 is slower than the average by ", averagespeed-speed3)
else:
    print ("Speed 3 is faster than the average speed by", speed3-averagespeed)