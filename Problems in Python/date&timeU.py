 
# CURRENT DATE TIME
from datetime import datetime,date,time,timedelta

nowTime=datetime.now()

#print(nowTime)

#FORMATTED DATES

formDate= nowTime.strftime("%Y-%m-%d %H:%M:%S")

#print("Formatted Date and Time is ,",formDate)

#PASRSING DATE

strdate= "2003-02-23 07:20:03"

parseDet= datetime.strptime(strdate,"%Y-%m-%d %H:%M:%S")

#print("\nparsed datetime is  , ",parseDet)

#delta time

delta  = timedelta(days=114,hours=12,minutes=32)

newdate= nowTime + delta

#print("Delta time of new date 'it was added' ",newdate)
newdate= nowTime - delta
#print("Delta time of new date 'it was reduced' ",newdate)

#Date Object
date1=date(2024,4,5)
date2=date(2003,2,23)

date3=date1-date2
date4=date1-date2

#print(f"\n date one 'added', {date3}\ndate two 'reduced' {date4}")


#TIME DIFFERENCE IN SECONDS

newnow=datetime.now()
newnow2=datetime.now()- timedelta(days=2,hours=6,minutes=20)

print(newnow2)











