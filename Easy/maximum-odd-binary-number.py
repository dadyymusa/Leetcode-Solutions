#Link - https://leetcode.com/problems/maximum-odd-binary-number/submissions/1215794469/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        zeroes = 0
        ones = 0
        res = ''
        for num in s:
            if num == '0':
                zeroes += 1
                print(f'zero:{zeroes}')
            elif num == '1':
                ones += 1
                print(f'one:{ones}')
        res = res + (ones - 1)*('1') + zeroes*('0') + '1'

        return res
        