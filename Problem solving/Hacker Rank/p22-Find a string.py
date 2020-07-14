def count_substring(string, sub_s):
    first = 0
    last = len(sub_s)
    count = 0


    while last <= len(string):
        if sub_s in string[first:last]:
            count += 1

        first = last-1
        last = last+2

    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)