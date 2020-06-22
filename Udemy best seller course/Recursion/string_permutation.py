def permutation(s):

    out = []

    # base case
    if len(s) == 1:
        return s

    else:
        # every letter in string
        for i, let in enumerate(s):

            for perm in permutation(s[:1])
