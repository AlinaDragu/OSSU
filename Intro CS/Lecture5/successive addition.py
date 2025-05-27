# successive addition

# 0.125 is a perfect power of 2
x = 0
for i in range(10):
    x += 0.125
print(x == 1.25)

# 0.1 is not a perfect power of 2
y = 0
for i in range(10):
    y += 0.1
print(y == 1)

print(y, '==', 10*0.1)