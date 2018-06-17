"""code written in python 3 by TARUN KUMAR on 17/06/2018
This code prints the alternating x characters in a string
example:
    inputs:
              ENVIRONMENTAL(string)
              3(distance)
    output:
              ENVNMEL

   The code should print the first 'x' characters then it should skip the following 'x' characters then
   it will print the next 'x' characters untill the size of string is reached
"""
a=input() #string input ##i/p
b=int(input()) # 'x'    ##i/p
v=''
c=0
while(c<=len(a)):
    i=c
    for i in range(i,i+b):
        if(i==(len(a))):
            break
        else:
            v=v+a[i]
            c=i
    c=c+b+1
print(v) # 'x' alternated string (o/p)
