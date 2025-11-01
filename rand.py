import random

# #randint
# count = int(input("total count: "))
# start = int(input("rand range low: "))
# end = int(input("rand range high: "))
# sum = 0
# for i in range(count):
#     rand = random.randint(start, end)
#     print(rand)
#     sum += rand
# print(f"sum is{sum}")
# avg = sum/count
# print(f"avg: {avg}")

# #random floating point
# count = int(input("total count: "))
# start = int(input("rand range low: "))
# end = int(input("rand range high: "))
# sum = 0
# for i in range(count):
#     rand = random.random(start, end) #start is inclusive, end not
#     print(rand)
#     sum += rand
# print(f"sum is{sum}")
# avg = sum/count
# print(f"avg: {avg}")

#heads or tails
seed = random.randint(0,1)
if seed == 0:
    print("\nHeads\n")
else:
    print("\nTails\n")
# #testing for uniform inclusivity
# while True:
#     rand = int(random.uniform(0,2))
#     print(rand)
#     if rand == 2:
#         break