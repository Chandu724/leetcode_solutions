class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        lst = []
        for start, end in intervals:
            lst.append((start, 1))
            lst.append((end, -1))
            
        print(lst)
        lst.sort()
        print(lst)
        
        res, curr_rooms = 0, 0
        
        for t, n in lst:
            print(t,n)
            curr_rooms += n
            res = max(res, curr_rooms)
        return res
            