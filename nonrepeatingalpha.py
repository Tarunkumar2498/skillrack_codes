"""this code prints the non repeating alphabets in a string
created on:14/06/2018 by TARUN KUMAR"""
A=input()  
l=len(A)
b=''
b=b+(A[0])
i=1
n=0
while(i<l):
    if(A[n]==A[i]):
        i=i+1
    else:
        n=i
        b=b+(A[i])
        i=i+1
print(b)
