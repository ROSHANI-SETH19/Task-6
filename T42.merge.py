def merge_intervals(intervals):
    # If no intervals are given, return an empty list
    if not intervals:
        return []
    
    # Step 1: Sort intervals based on the start time
    intervals.sort(key=lambda x: x[0])
    
    # Step 2: Initialize the merged intervals list with the first interval
    merged = [intervals[0]]
    
    # Step 3: Iterate through the intervals and merge when necessary
    for current in intervals[1:]:
        # Compare the current interval with the last interval in the merged list
        last_merged = merged[-1]
        
        if current[0] <= last_merged[1]:
            # There is an overlap, so merge the intervals
            last_merged[1] = max(last_merged[1], current[1])
        else:
            # No overlap, add the current interval to the merged list
            merged.append(current)
    
    return merged

# Example usage:
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merged_intervals = merge_intervals(intervals)
print("Merged intervals:", merged_intervals)
