left_list = []
right_list = []

with open('input.txt', 'r') as file:
    for line in file:
        col_left, col_right = line.strip().split()
        left_list.append(col_left)
        right_list.append(col_right)

left_list.sort()
right_list.sort()
total_difference = 0
length = len(right_list) # storing the length of the lists


for i in range(length):
    print(f"{int(right_list[i])} - {int(left_list[i])} = {int(right_list[i])-int(left_list[i])}\n")
    print(f"Current Total Difference: {total_difference}\n")
    total_difference = abs(int(right_list[i]) - int(left_list[i])) + total_difference
print(f"Total difference: {total_difference}\n")
        
# PART ONE CORRECT SOLUTION

