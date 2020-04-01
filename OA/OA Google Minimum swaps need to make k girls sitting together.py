'''
Google | Minimum swaps need to make k girls sitting together



Given a string contains only "B"s and "G"s indicated a sequence of students, 
while "B" means a boy and "G" means a girl. 
Write a function called minSwaps(students, k) to 
calculate the minimum swaps need to make k girls sitting together. 
Note that you could only swap two students if they are adjacent.

Example 1:

Input: students = "BGGBBG", k = 3
Output: 2
Example 2:

Input: students = "BGGBGBGBBGGG", k = 4
Output: 2
'''


def min_swaps_all(students):   # min swaps to make all girls sitting together
    cnt_girls = students.count('G')
    cnt_swaps = 0
    left, right = 0, len(students)-1
    while left < right:
        if students[left] != "G":
            left += 1
        elif students[right] != "G":
            right -= 1
        else:
            cnt_girls -= 2
            cnt_swaps += (right-left-1)-cnt_girls
            left += 1
            right -= 1
    return cnt_swaps


def min_swaps_k(students):
    pass



for students in ["BGGBBG", "BGGBGBGBBGGG"]:
    print(min_swaps_all(students))

