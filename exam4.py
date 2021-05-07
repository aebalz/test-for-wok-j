# Test Exam 4

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


n = 10                      # n ห้ามน้อยกว่า 1
number = factorial(n)
str_number = str(number)
count = 0
while True:
    if str_number[-1] == "0":
        str_number = str_number[:-1]
        count += 1
    else:
        print(f"factorial : {n}! [{number}]")
        print(f"count : {count}")
        break
