import random

dummy_data = [138, 15, 159, 124, 15, 19, 195, 68, 8, 175, 126, 180, 95, 2, 68, 125, 31, 6, 29,205,112, 152]
# for loop for a list
max = 0
for data in dummy_data:
    if data > max:
        max = data
    
print(max)


# for loop with range function
sum = 0
for i in range(1,101):
    sum += i

print(sum)