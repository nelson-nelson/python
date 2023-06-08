"""
Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


def lcp(l: list) -> str:
    str1 = l[0]
    for i in range(len(str1)):
        cp = str1[:len(str1)-i]
        for s in l[1:]:
            if not s.startswith(cp):
                cp = ""
                break
        if cp:
            return cp
    return ""


if __name__ == '__main__':
    l = ["flower", "flow", "flight"]
    print(lcp(l))
    l = ["dog","racecar","car"]
    print(lcp(l))
    l = ['plow', 'flower', 'flight']
    print(lcp(l))
