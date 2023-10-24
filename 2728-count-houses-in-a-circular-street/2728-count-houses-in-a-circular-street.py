# Definition for a street.
# class Street:
#     def openDoor(self):
#         pass
#     def closeDoor(self):
#         pass
#     def isDoorOpen(self):
#         pass
#     def moveRight(self):
#         pass
#     def moveLeft(self):
#         pass
class Solution:
    def houseCount(self, street: Optional['Street'], k: int) -> int:
        
        x=0
        res = 0
        
        for i in range(k):
            street.closeDoor()
            street.moveRight()
            
        while x >= 0:
            if street.isDoorOpen():
                x = -1
            else:
                street.openDoor()
                street.moveRight()
                res = res + 1
                
        return res