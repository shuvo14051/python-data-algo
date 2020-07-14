import textwrap

def wrap(string, max_width):
    r = ''
    s = textwrap.wrap(string, max_width)
    for i in s:
        r = r+i+"\n"
    return r


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)