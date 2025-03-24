def maxSubArray(nums):
    # Initialize the variables
    max_sum = float('-inf')  # Start with the smallest possible value
    current_sum = 0
    
    # Iterate through each number in the array
    for num in nums:
        # Update current_sum by including the current element or starting new subarray
        current_sum = max(num, current_sum + num)
        
        # Update max_sum with the largest sum encountered so far
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum sum of contiguous subarray:", maxSubArray(nums))
