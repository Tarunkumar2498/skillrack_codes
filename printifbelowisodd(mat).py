"""program id-5793 print integer if below is odd
   Integer matrix R*C is given as input.The program must print the integer if the integer present below
the current integer is odd else print '*'
    Boundary conditions:
           2<=R ; C<=10
    Input format
           first line contains r and c splitted by space
           following r lines will contain inputs to matrix splitted by space
     Example1:
         input:
              2 3
              3 4 5
              6 7 8
         output:
              * 4 *
              * * *
     Example2:
         input:
             3 3
             2 6 72
             4 3 1
             1 6 9
         output:
             * 6 72
             4 * 1
             * * *
This code was created by TARUN KUMAR on 18/06/2018.For further queries reach me at  tarunkumar2498[at]google[dot]com"""
#code begings here
r,c=input().split()#inputs
r=int(r)
c=int(c)
m1=[]
for i in range(0,r):
    m1.append([int(x)for x in input().split()]) #matrix(m1) input
for i in range(0,r-1):
    for j in range(0,c):
        if(((m1[i+1][j])%2)==1):
            print(m1[i][j],end=' ')
        else:
            print('*',end=' ')
    print()
for k in range(0,c):
    print('*',end=' ')