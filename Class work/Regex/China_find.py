import re

with open('China space') as f:
    china = f.read()

a = re.findall('[a-zA-Zа-яА-ЯёЁ]+\-[1-9]+', china)
b = set(a)
print (sorted(b))

c = re.findall('(«.+?»).+?\s\(кит\..+?\)', china)

print (set(c))

# луноход, ракет, марсианская межпланетная станция, космоплан,
# не обязатльно в кавычках: Дунфан Хун-1 (спутник)
# не обязательно с цифрами: космоплана «Шэньлун». луноходом «Юйту»

