import random

#randint
count = int(input("total count: "))
start = int(input("rand range low: "))
end = int(input("rand range high: "))
sum = 0
for i in range(count):
    rand = random.randint(start, end)
    print(random.randint(start,end))
    sum += rand
print(f"sum is{sum}")
avg = sum/count
print(f"avg: {avg}")

#random floating point