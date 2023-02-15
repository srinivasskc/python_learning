# If it's even number, skip the process

for i in range(1, 5):
    if i % 2 == 0:
        continue
    print(i*i)
