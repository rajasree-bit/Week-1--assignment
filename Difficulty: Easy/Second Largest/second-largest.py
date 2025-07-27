class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        
        largest = second = -1
        for num in arr:
            if num > largest:
                second = largest
                largest = num
            elif num != largest and num > second:
                second = num
        return second if second != -1 else -1

