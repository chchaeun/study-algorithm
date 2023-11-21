from collections import defaultdict

num_of_numbers = [0 for _ in range(10)]

room_number = input()

for rn in room_number:
    integer = int(rn)

    if integer in [6, 9]:
        if num_of_numbers[6] >= num_of_numbers[9]:
            num_of_numbers[9] += 1
        else:
            num_of_numbers[6] += 1
    else:        
        num_of_numbers[int(rn)] += 1

print(max(num_of_numbers))