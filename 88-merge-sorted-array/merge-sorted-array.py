class Solution:
    def merge(self, arr1: List[int], m: int, arr2: List[int], n: int) -> None:
        arr1mptr = m - 1
        arr1rptr = m + n - 1
        arr2rptr = n - 1

        while True:
            if arr1mptr < 0:
                for i in range(arr2rptr+1):
                    arr1[i] = arr2[i]
                break
            
            elif arr2rptr < 0:
                break

            else:
                if arr1[arr1mptr] > arr2[arr2rptr]:
                    arr1[arr1rptr] = arr1[arr1mptr]
                    arr1mptr -= 1
                else:
                    arr1[arr1rptr] = arr2[arr2rptr]
                    arr2rptr -= 1
                arr1rptr -= 1
