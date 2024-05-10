import urllib.request
print(type(urllib.request)) # 별칭을 사용하지 않은 경우

import urllib
print(type(urllib))

import myPackage.moduleA
myPackage.moduleA.functionA()

# from myPackage import *
# moduleA.functionA()

from myPackage import *