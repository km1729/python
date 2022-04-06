from datetime import date
import os
import re

dir='/home/kelly/0tutorials/todayfile'

t = date.today()
st = str(date.today())
pattern = re.compile('\d{4}-\d{2}-\d{2}')

for l in os.listdir(dir):
    match_group = pattern.match(l)
    if match_group :
        if match_group.group() == st:
            print(l)
