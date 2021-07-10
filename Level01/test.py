import re

a = '12,345'

b = re.sub('[^0-9]', '', a)
print(b)