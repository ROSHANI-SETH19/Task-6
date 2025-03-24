def findMedianSortedArrays(nums1, nums2):
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    # Get lengths of both arrays
    len1, len2 = len(nums1), len(nums2)
    
    # Binary search on the smaller array
    low, high = 0, len1
    
    while low <= high:
        # Partition nums1 and nums2
        partition1 = (low + high) // 2
        partition2 = (len1 + len2 + 1) // 2 - partition1
        
        # Find the max of left side and min of right side
        maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        minRight1 = float('inf') if partition1 == len1 else nums1[partition1]
        
        maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
        minRight2 = float('inf') if partition2 == len2 else nums2[partition2]
        
        # Check if we have found the correct partition
        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
            # If the combined length is odd, the median is the max of left side
            if (len1 + len2) % 2 == 1:
                return max(maxLeft1, maxLeft2)
            # If the combined length is even, the median is the average of the max of left side and min of right side
            return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
        elif maxLeft1 > minRight2:
            # If maxLeft1 is too big, move the partition in nums1 to the left
            high = partition1 - 1
        else:
            # If maxLeft2 is too big, move the partition in nums1 to the right
            low = partition1 + 1
    
    # If no partition is found (which shouldn't happen if the input is correct)
    raise ValueError("Input arrays are not sorted correctly or contain invalid elements.")

# Example usage:
nums1 = [1, 3]
nums2 = [2]
print("Median:", findMedianSortedArrays(nums1, nums2))  # Output: 2.0

nums1 = [1, 2]
nums2 = [3, 4]
print("Median:", findMedianSortedArrays(nums1, nums2))  # Output: 2.5
