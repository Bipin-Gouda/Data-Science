'''RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.'''

import re
print('\n')

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

if x:
  print("YES! We have a match!")
else:
  print("No match")

lst=['Hello sir how are you', ' I am fine Thank you']
print(lst.str.extract(pat='[A-Za-z]i.'))  # can be used for a series of strings but not a string and the condn
                                       # will be applies to every  string