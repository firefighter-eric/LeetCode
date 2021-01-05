from queue import PriorityQueue

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists) -> ListNode:
        ans = cur = ListNode()
        pq = PriorityQueue()
        for index, l in enumerate(lists):
            if l:
                pq.put((l.val, index))

        while not pq.empty():
            _, index = pq.get()
            l = lists[index]
            if l.next:
                pq.put((l.next.val, index))
            cur.next = l
            lists[index] = lists[index].next
            cur = cur.next

        return ans.next


if __name__ == '__main__':
    # L = [[1, 4, 5], [1, 3, 4], [2, 6]]
    Lists = [ListNode(1, ListNode(4, ListNode(5))),
             ListNode(1, ListNode(3, ListNode(4))),
             ListNode(4, ListNode(6)),
             ]

    s = Solution()
    ans = s.mergeKLists(Lists)
    while ans:
        print(ans.val)
        ans = ans.next
