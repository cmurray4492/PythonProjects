# Sum all natural numbers between 1 and 1000 that can be
# divided equally by 3 and 5.

summed = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        summed = summed + i

print(summed)

# Or a different approach
# below uses a list which is less efficent - uses memory

x = sum([n for n in range(1, 1000) if n % 3 == 0 or n % 5 == 0])
print(x)
