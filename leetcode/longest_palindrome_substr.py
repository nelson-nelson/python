"""
longest non repeating substring
"""


def lrs(s: str) -> str:
    for i in range(len(s)):
        max_len = len(s) - i
        print(f'{i} -- {max_len}')
        j = 0
        while j <= len(s) - max_len:
            s1 = s[j:max_len + j]
            print(f's1 is {s1}')
            s2 = s1[::-1]
            print(f's2 is {s2}')
            if s1 == s2:
                return s1
            j += 1


if __name__ == '__main__':
    s = 'babad'
    s1 = lrs(s)
    print(s1)
