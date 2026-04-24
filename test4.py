visitors = ["user123","coco7","user123","nina99","coco7","jiyeon_lee","user123"]
unique_visitors = set(visitors)
print(len(unique_visitors))

all_students = {"지연","민수","혜라","철수","영희"}

submitted = {"지연","혜라","영희"}
not_submitted = all_students - submitted
print(len(not_submitted))

not_submitted_list = list(not_submitted)
print(not_submitted_list)