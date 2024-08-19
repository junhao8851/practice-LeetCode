class Solution:
    def reverseWords(self, s: str) -> str:

         words = reversed(s.split()) #split()把一个字符串以默认空格符为界进行分隔，返回一个列表，与join()刚好相反

         """
         words列表的reversed操作也可以用双指针实现：
         left, right = 0, len(words) - 1
         while left < right:
         words[left], words[right] = words[right], words[left]
         left += 1
         right -= 1
     
         """

         return ' '.join(words)      # join()方法把列表，元组各元素用某个字符串拼接起来，返回一个字符串

