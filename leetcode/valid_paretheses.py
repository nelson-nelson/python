"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


def validate_paretheses1(s: str) -> bool:
    s1 = s
    while (len(s) > 0) and (len(s1) == len(s)):
        s = s.replace('()', '')
        s = s.replace('{}', '')
        s = s.replace('[]', '')
        s1 = s
    return len(s) == 0


def validate_paretheses2(s: str) -> bool:
    mapping = {
        ')': '(',
        ']': '[',
        '}': '{',
        '(': '-',
        '[': '-',
        '{': '-',
    }
    s1 = [s[0]]
    for c in s[1:]:
        if s1[-1] == mapping[c]:
            s1.pop()
        else:
            s1.append(c)
    return len(s1) == 0


if __name__ == '__main__':
    s = "[()([]{})]"
    print(validate_paretheses1(s))
    print(validate_paretheses2(s))
