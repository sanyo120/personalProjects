#Given
##string s
##sub string k
#Task
##Print all starting and ending indices (inclusive) where k occurs in s, including overlapping matches.
##If no match is found, return (-1, -1).
import re
s = input()
k = input()
pattern = f'(?={k})'
matches = list(re.finditer(pattern,s))
if matches:
    for match in matches:
        start = match.start()
        end = start + len(k)-1
        print ((start, end))
else:
    print ((-1, -1))