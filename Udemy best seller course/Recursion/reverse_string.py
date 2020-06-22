"""
#Using slicing
def reverse_string(s):
    return s[::-1]


result = reverse_string("shuvi ji the boss")
print(result)
"""


def reverse(s):

    # base case
    if len(s) == 1:
        return s

    return reverse(s[1:]) + s[0]


result = reverse("abc")
print(result)
