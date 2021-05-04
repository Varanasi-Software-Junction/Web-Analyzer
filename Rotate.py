a = 8
b = 12
while a % b != 0:
    t = a % b
    a=b
    b=t
print(b)