n = int(input())
li = []
for i in range(n):

    option = input()

    if option == "insert":
        position, item = input().split()
        position = int(position)
        item = int(item)
        li.insert(position, item)

    elif option == "append":
        item = int(input())
        li.append(item)

    elif option == "pop":
        li.pop()

    elif option == "print":
        print(li)

    elif option == "remove":
        item = int(input())
        li.remove(item)

    elif option == "sort":
        li.sort()

    elif option == "reverse":
        li.reverse()
