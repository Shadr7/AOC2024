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

# Calculate a total similarity score by adding up each number
# in the left list after multiplying it by the number of times that number appears in the right list.
similarity_score = 0
appear_count = 0
# check how many times left_list[i] is in right_list (appear_count)
# multiply left_list[i] by appear_count
# appear_count = 0, repeat for next i

for i in range(length):
    if left_list[i] in right_list:
        for j in range(length):
            if left_list[i] == right_list[j]:
                appear_count += 1
        similarity_score = similarity_score + (int(left_list[i]) * appear_count)
        appear_count = 0
    else:
        continue

print(f"Similarity Score: {similarity_score}")


# PART TWO CORRECT SOLUTION