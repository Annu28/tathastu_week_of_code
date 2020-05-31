class Sol(obj):
    def mergeLists(self, lists):
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

    def merge2Lists(self, l1, l2):
        head = qr = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                qr.next = l1
                l1 = l1.next
            else:
                qr.next = l2
                l2 = l1
                l1 = qr.next.next
            qr = qr.next
        if not l1:
            qr.next=l2
        else:
            qr.next=l1
        return head.next
