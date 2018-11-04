import re

string = ('Hi there ')

regex_pattern = r'([a-zA-Z]+(?=( )))'

#r'(?=[a-zA-Z]+)(?=( |))'

print (str(re.findall(regex_pattern, string)))