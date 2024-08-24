class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: 
            return []

        phone = {'2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'],
                 '5':['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'],
                 '9':['w','x','y','z']}

        res = []  

        def backtrack(conbination,next_digit):
            if len(next_digit) == 0:
                res.append(conbination)
            else:
                for letter in phone[next_digit[0]]:
                    backtrack(conbination + letter,next_digit[1:])

        backtrack('',digits)
        return res
