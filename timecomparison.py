"""                     TIME COMPARISON
   The following code is written to perform time comparisons
   The input being a set of time that are to be compared with a particular time value
   here i have taken 10:00 as the value for comparison it can be changed according to your requirements
   to have the present time in your code use datetime.datetime.now()
Question:
    print the number of entries above 10:00 in the following time data
     Input:
        string containing various time separated by space
     Output:
        count of time higher than 10:00
    Example:
         i/p:
           10:00 09:55 11:00 10:20
         o/p:
            2
This code was created by TARUN KUMAR on 18-06-2018
for further queries reach me at  tarunkumar2498[at]gmail[dot]com
"""
#code begins here
import datetime  #library for datetime
t=[x for x in input().split()] #i/p
a=len(t)
c=0
dnow = datetime.datetime.strptime('10:00','%H:%M')
for i in range(0,a):
    d = datetime.datetime.strptime(t[i],'%H:%M')
    if d.time()>dnow.time():
        c=c+1
print(c)
##end##