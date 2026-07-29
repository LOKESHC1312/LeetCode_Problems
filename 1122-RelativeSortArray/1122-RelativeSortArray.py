# Last updated: 7/29/2026, 12:24:40 PM
1class Solution:
2    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
3        answer=[]
4        for i in arr2:
5            while i in arr1:
6                answer.append(i)
7                arr1.remove(i)
8        arr1.sort()
9        return answer+arr1