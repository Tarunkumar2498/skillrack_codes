"""ProgramID-5872
                   Matrix Next Greatest Column Element
    A matrix of size R*C is given as input. The program must print the next
    greatest number present below each of the numbers. The number must also be
    an odd number .If there is no odd element which is also greater than current
    element present below then print '*'
      BoundaryCondition(s):
            1<=N<=1000
      InputFormat:
            The first line contains R and C separated by space
            The next R lines countain C elements separated by space
    Example 1:
        i/p:
          3 3
          1 2 3
          4 5 6
          7 8 9
        o/p:
          7 5 9
          7 * 9
          * * *
    Example 2:
        i/p:
        4 5
        46 45 -4 98 -88
        77 -44 15 -56 43
        43 -27 18 13 16
        -73 -99 -78 56 15
        o/p:
        77 * 15 * 43
        * -27 * 13 *
        * * * * *
        * * * * *
This code was created by TARUN KUMAR on 19-06-2018 08:20 IST .
For further queries reach me at  tarunkumar2498[at]google[dot]com
coded in python3
"""
#code begings here
r,c=input().split()#inputs
r=int(r)
c=int(c)
m1=[]
b=[]
for i in range(0,r):
    m1.append([int(x)for x in input().split()]) #matrix(m1) input
for i in range(0,r-1):
    for j in range(0,c):
        for k in range(i+1,r):
            if(((m1[k][j])%2)==1 and m1[k][j]>m1[i][j]):
                b.append(m1[k][j])
        if(len(b)!=0):
                print(max(b),end=' ')
        else:
                print('*',end=' ')
        b=[]
    print()
for k in range(0,c):
    print('*',end=' ')
##end##