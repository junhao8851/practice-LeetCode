class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        #贪心的点在于收到20美元时尽量用10+5，而不是3张5
        fives = 0
        tens = 0
        twentys = 0
        
        for bill in bills:
            # 情况一：收到5美元
            if bill == 5:
                fives += 1
            
            # 情况二：收到10美元
            if bill == 10:
                if fives <= 0:
                    return False
                tens += 1
                fives -= 1
            
            # 情况三：收到20美元
            if bill == 20:
                # 先尝试使用10美元和5美元找零
                if fives > 0 and tens > 0:
                    fives -= 1
                    tens -= 1
                    twentys += 1
                # 如果无法使用10美元找零，则尝试使用三张5美元找零
                elif fives >= 3:
                    fives -= 3
                    twentys += 1
                else:
                    return False
        
        return True