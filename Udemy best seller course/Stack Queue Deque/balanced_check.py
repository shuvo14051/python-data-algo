def balanced_check(s):

    if len(s) % != 0:
        return False
    
    opening = set('({[')

    matches = set()

    stack = []

    for parent in s: 