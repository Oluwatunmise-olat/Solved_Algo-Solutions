"""
************** QUESTION***************
Find the angle between the hour and minutes hands  of a clock, given the time
time format is Hour:min
"""


"""
My Explanation

Now in a clock we have 12 unique degrees that can be likened to that of a cartesian plane going in the clockwise direction now.
Hence we can say
Hours = {
    '0':0deg, '1':30deg, '2':60deg, '3':90deg, '4':120deg,
    '5':150deg, '6':180deg, '7':210deg, '8':240deg,
    '9':270deg,'10':300deg, '11':330deg, '12':360deg
}
that should make sense so also we can do the same for minutes
Minutes = {
    '0':0deg, '5':30deg, '10':60deg, '15':90deg, '20':120deg,
    '25':150deg, '30':180deg, '35':210deg, '40':240deg,
    '45':270deg,'50':300deg, '55':330deg, '60':360deg
}
wow that was draining right 😂.
Now we can choice to index each hour, minutes and get the degree from the dictonary above but we could do better.

******MINUTES*****
Minutes simple all you need to do to get the degree IS MULTIPLY BY 6 just follow the Minutes dictionary and try it out you will see you get the same answer.

*****IF YOU LIKE STRESS :)******

Now there is a more technical way to do these . eg if you have something like 57 min or 49 mins [What i said about multiplying by 6 still holds] you could
split you calculation of minutes to be (taken 57mins) 50 and check the degree of that in the miutes dictionary above the 7 minutes
or whatever value you might have there can be gotten in minutes by multiplying the valu by 6 and adding to the deg of 50
Reason being, between to consecutive minutes e.g 9,10 [45,50] we have 5 values between them and since THE DEGREE BETWEEN TWO CONSECUTIVE
NUMBER IS 30 DEG, the varying values i.e(45->46, 46->47, 47->48, 48->49, 49->50) would each represent 6 degrees
Now you can see the technicallity right

so 49 minutes = equivalent of 40min in degree refer to the miutes dictionary + 9 *6

******MINUTES*******
we see that if you multiply the hour by 30 we get the degree. That much better.
HOUR = HOUR* 30 + MINUTES/2

*****IF YOU LIKE STRESS:)******

now pay attention it gets a bit tricky here.

Take for example the time wants to change from 4:00 to 5:00. THE SECS HAND HAS TO GO THRU 60 REVOLUTIONS WHICH EQUATES TO 3,600 SECS
FOR A ONE 1 MINUTE CHANGE

SINCE 60 SECS = 1 COMPLETE REVOLUTION FROM 0 TO 12

AND 60 SECS = 1MIN(1 COMPLETE REVOLUTION)
HENCE IT TAKEs 60 MINS(60REVS) which is equivalent to 30DEG[IF YOU LOOK AT THE DICTIONARY I DID ABOVE YOU NOTICE THAT THE DISTANCE BETWEEN TO CONSECUTIVE POINTS IS 30DEG] HENCE WITH THAT,
to make the hour angle complete we take the min and divide by 2(i would explain this soon)

Hence hour = hour * 30 + minutes/2

i said i would explain the minutes/2 .
here we go. if you followed my earlier explainion you should get this now.

SINCE 60 [REV||MIUTES]= 30 DEG[IF YOU LOOK AT THE DICTIONARY I DID ABOVE YOU NOTICE THAT THE DISTANCE BETWEEN TO CONSECUTIVE POINTS IS 30DEG]
THEN M MINUTES = X DEG
CROSS MULTIPLY YOU GET (M(in minutes)*30)/60 WHICH GIVES THE DEGS MOVED BY THE SHORTHAND FOR THE GIVEN MINUTES


"""


def AngleBetweenLongAndShort(time_: str):
    output: int
    time_ = time_.split(':')
    hour = time_[0]
    minute = time_[1]

    if int(hour) > 12:
        hour = int(hour) - 12

    hourAngle = int(hour) * 30 + (int(minute)/2)
    minuteAngle = int(minute) * 6

    return abs(hourAngle - minuteAngle)


print(AngleBetweenLongAndShort('9:33'))
