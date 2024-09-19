class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:

        #局部最优：把people按身高降序，身高相同的按k升序，之后优先按照身高高的人的k值来决定插入位置，符合要求

        people.sort(key = lambda x :(-x[0] , x[1]))
        queue = []

        for i in people:
            queue.insert(i[1] , i)
        
        return queue
