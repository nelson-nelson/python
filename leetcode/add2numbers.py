"""
Add 2 numbers.
Example:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""


class Num:
    def __init__(self, l: list):
        self.digits = l

    @classmethod
    def add(cls, num1, num2) -> list:
        len1 = len(num1.digits)
        len2 = len(num2.digits)
        maxlen = len1 if len1 > len2 else len2
        print(f'maxlen is {maxlen}')
        sum = [0] * (maxlen + 1)
        print(f'initialize sum to {sum}')
        for j in range(maxlen):
            i = maxlen - j - 1
            d1 = num1.digits[i] if i < len1 else 0
            d2 = num2.digits[i] if i < len2 else 0
            sum_d = d1 + d2
            sum[j] += sum_d % 10
            sum[j+1] += sum_d // 10
        if sum[-1] == 0:
            sum.pop(-1)
        return sum


if __name__ == '__main__':
    num1 = Num([2, 4, 3])
    num2 = Num([5, 6, 4])
    sum = Num.add(num1, num2)
    print(f'sum is {sum}')

