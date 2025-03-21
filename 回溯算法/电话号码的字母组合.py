    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        result = [""]
        dict = {2: ['a','b','c'], 3:['d','e','f'], 4: ['g','h','i'], 5: ['j','k','l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u' , 'v'], 9: ['w', 'x', 'y', 'z']}
        for item in digits:
            temp_list = []
            for i in dict[int(item)]:
                for j in result:
                    temp_list.append(j + i)
            result = temp_list
        return result

