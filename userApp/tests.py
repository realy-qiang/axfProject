from django.test import TestCase
import re

# Create your tests here.
str1 = 'k:1|k1:2|k2:3|k3:4'

dict1 = {}

for items in str1.split('|'):
    key, value = items.split(':')
    dict1[key] = value

print(dict1)

# qpucnbaiuijzicid
# cvataumvtltyjhij