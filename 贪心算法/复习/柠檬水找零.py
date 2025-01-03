class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for b in bills:
            if b == 5:  # 无需找零
                five += 1
            elif b == 10:  # 返还 5
                five -= 1
                ten += 1
            elif ten:  # 此时 b=20，返还 10+5
                five -= 1
                ten -= 1
            else:  # 此时 b=20，返还 5+5+5
                five -= 3
            if five < 0:  # 无法正确找零
                return False
        return True

作者：灵茶山艾府
链接：https://leetcode.cn/problems/lemonade-change/solutions/2353707/fen-lei-tao-lun-jian-ji-xie-fa-pythonjav-37oe/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。