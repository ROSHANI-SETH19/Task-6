def maximalRectangle(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    # Initialize the heights array for the histogram
    n = len(matrix[0])
    heights = [0] * n
    max_area = 0

    # Iterate through each row of the matrix
    for row in matrix:
        # Update the histogram heights
        for i in range(n):
            # If the current cell is 1, add 1 to the height, else reset to 0
            heights[i] = heights[i] + 1 if row[i] == '1' else 0
        
        # Compute the largest rectangle in the histogram (heights)
        max_area = max(max_area, largestRectangleInHistogram(heights))
    
    return max_area

def largestRectangleInHistogram(heights):
    # Stack-based approach to find the largest rectangle in histogram
    stack = []
    max_area = 0
    heights.append(0)  # Append 0 to ensure we can pop all elements at the end

    for i in range(len(heights)):
        # Maintain a monotonically increasing stack
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        
        stack.append(i)
    
    return max_area

# Example usage:
matrix = [
    ['1', '0', '1', '0', '0'],
    ['1', '0', '1', '1', '1'],
    ['1', '1', '1', '1', '1'],
    ['1', '0', '0', '1', '0']
]

print("Maximal rectangle area:", maximalRectangle(matrix))
