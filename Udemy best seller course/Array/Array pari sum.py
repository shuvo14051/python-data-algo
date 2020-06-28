def pair_sum(li, k):

    if len(li) < 2:
        print( "There is no pair.")

    # sets for tracking
    seen = set()
    output = set()

    for num in li:
        target = k-num

        if num not in seen:
            seen.add(num)
        else:
            output.add(((min(num,target)), max(num,target)))

    print('\n' .join(map(str, list(output))))


pair_sum([1,3,3,1] ,4)
