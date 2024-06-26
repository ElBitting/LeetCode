#A very naive solution. Have ideas on how to improve via recursion

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return list1
            
        temp = []
        while list1 and list2:
            if list1.val <= list2.val:
                temp.append(list1.val)
                list1 = list1.next
            else:
                temp.append(list2.val)
                list2 = list2.next

        while list1:
            temp.append(list1.val)
            list1 = list1.next
        while list2:
            temp.append(list2.val)
            list2 = list2.next
        
        temp = temp[::-1]
        temp2 = ListNode()

        for i in range(len(temp)):
            final = ListNode()
            final.val = temp[i]
            if i > 0:
                final.next = (temp2)
            temp2 = (final)
        return final
