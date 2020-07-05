def is_even(num):
    if num %2 == 0:
        return True
    return False

user_input = int(input("Enter a number:"))
li = []

for i in range(2,user_input+1,2):
    if is_even(i):
        li.append(i)

print(li)
