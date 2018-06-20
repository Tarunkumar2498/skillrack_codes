"""ProgramID-5871
        DISCOUNT SLABS
    A shop has given discount based on the price of purchase.There are N slabs.
    When the price falls between two slabs that is ith slab amount and i+1th slab
    amount then the discount for the ith slab is applied.Given the price of purchase
    print the discounted amount to pay with precision up to two decimal places.
       Boundary Conditions:
            1<=N<=100
        InputFormat:
          The first line contains N and price of purchase separated by space
          The second line contains N slabs separated by space
          The third line contains N discounts separated by space
        OutputFormat:
          The First line contains discounted price rounded to two decimal places
        Example 1:
           i/p:
             4 3400
             1000 2000 3000 4000
             12 16 18 24
           o/p:
             2788.00
            Explanation:
                18% is applied since 3400 lies between 3000 and 4000
        Example 2:
           i/p:
             4 400
             500 1000 1500 2000
             10 20 30 40
           o/p:
             400.00
            Explanation:
              no discount since it doesnt fall between any slabs
This code was written by TARUN KUMAR on 20/06/2018 08:30(IST)
For further Queries reach me at tarunkumar2498[at]gmail[dot]com
Code written in Python 3
"""
#code begings here
a,b=input().split()  # N and price i/p
a=int(a)
b=float(b)
c=[]
d=[]
c=[float(x) for x in input().split()] # N slabs i/p
d=[int(y) for y in input().split()]   # N discount i/p
di=0
am=0
for i in range(0,a-1):
    if(c[i]<=b and b<c[i+1]):
        di=(d[i]/100) * b
        am=b-di
        break
if(di==0):
    di=(d[a-1]/100)*b
    am=b-di
if(b<c[i]):
    print("%.2f"%b)
else:
    print("%.2f"%am)
##end##