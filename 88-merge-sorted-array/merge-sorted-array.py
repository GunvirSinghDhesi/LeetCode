class Solution:
    def merge(self, arr1: List[int], m: int, arr2: List[int], n: int) -> None:
        arr1rptr = m + n - 1
        
        m = m - 1
        
        n = n - 1

        while True:
            if m < 0:
                for i in range(n+1):
                    arr1[i] = arr2[i]
                break
            
            elif n < 0:
                break

            else:
                if arr1[m] > arr2[n]:
                    arr1[arr1rptr] = arr1[m]
                    m -= 1
                else:
                    arr1[arr1rptr] = arr2[n]
                    n -= 1
                arr1rptr -= 1
