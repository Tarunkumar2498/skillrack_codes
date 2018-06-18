"""           REMOVING DUPLICATES IN A STRING
      This code removes duplicates in a string
      Input:
         contains a string
      Output:
         string that contains only unique characters
    Example:
        i/p:
            "thisiscodedinpython3"
        o/p:
              thiscodenpy3
This code was created by TARUN KUMAR on 18/06/2018
for further queries reach me at  tarunkumar2498[at]gmail[dot]com
coded on python3
"""
#code begings here
from collections import OrderedDict
ip=input()
print ("".join(OrderedDict.fromkeys(ip)))
##end##