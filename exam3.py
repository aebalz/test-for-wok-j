# Test Exam 3

list_test = [7,2,1,3,5,16,4,5]

max_number = list_test[0]
index_number = 0
for i in range(1, len(list_test)):
    if list_test[i] > max_number:
        max_number = list_test[i]
        index_number = i
else:
    print(f"index : {index_number}")
