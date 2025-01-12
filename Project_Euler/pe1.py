# Sum all natural numbers between 1 and 1000 that can be
# divided equally by 3 and 5.

summed = 0
for i in range(1, 1001):
    if i % 3 == 0 and i % 5 == 0:
        summed = summed + i

print(summed)
