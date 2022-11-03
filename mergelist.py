from typing import List, Optional


class Solution():
    def mergeTwoLists(self, list1: List[int] , list2: List[int] ) -> List[int]:
        merged_list = list1
        for i in list2:
            merged_list.append(i)
        merged_list.sort()
        print(merged_list)
solution_1 = Solution()
solution_1.mergeTwoLists([1,2, 4], [1, 3, 4])
