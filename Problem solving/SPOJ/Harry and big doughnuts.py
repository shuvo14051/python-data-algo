test = int(input())
for i in range(test):
    cat, capacity, weight = map(int, input().split())
    if cat*weight <= capacity:
        print("yes")
    else:
        print("no")
