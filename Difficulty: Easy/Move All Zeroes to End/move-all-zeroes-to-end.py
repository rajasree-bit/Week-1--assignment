#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	n = len(arr)
        count = 0  # Position tracker for non-zero elements

        for i in range(n):
            if arr[i] != 0:
                arr[count], arr[i] = arr[i], arr[count]
                count += 1

        return arr