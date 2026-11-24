import random
#who pays the bill

friends =["alice", "vimal", "ben", "goki", "kathir", "jack"]

# own solution
seed = random.randint(0,5)
print(friends[seed])

# documentation
print(random.choice(friends))