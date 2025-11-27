import random

dummy_data = [138, 15, 159, 124, 15, 19, 195, 68, 8, 175, 126, 180, 95, 2, 68, 125, 31, 6, 29,205,112, 152]

max = 0
for data in dummy_data:
    if data > max:
        max = data
    
print(max)