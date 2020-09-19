import re

href = '//item.jd.com/100014522796.html'

re_01 = re.compile(r'\d+')

number = re_01.findall(href)

print(number)