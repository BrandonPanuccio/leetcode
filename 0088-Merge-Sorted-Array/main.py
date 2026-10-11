class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_ptr = m-1
        nums2_ptr = n-1
        write_ptr = m + n - 1
        
        while (nums2_ptr >= 0):
            if nums1_ptr >= 0 and nums1[nums1_ptr] > nums2[nums2_ptr]:
                nums1[write_ptr] = nums1[nums1_ptr]
                nums1_ptr -= 1
            else:
                nums1[write_ptr] = nums2[nums2_ptr]
                nums2_ptr -= 1
            write_ptr -= 1

if __name__ == '__main__':
    solution = Solution()
    nums1 = [1,2,3,0,0,0]
    solution.merge(nums1, m = 3, nums2 = [2,5,6], n = 3)
    print(nums1)