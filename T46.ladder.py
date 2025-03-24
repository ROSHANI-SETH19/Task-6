from collections import deque

def wordLadder(start, end, wordList):
    # If the end word is not in the dictionary, return 0 (no valid transformation)
    if end not in wordList:
        return 0
    
    # Initialize the queue for BFS and a visited set
    queue = deque([(start, 1)])  # (current_word, current_depth)
    visited = set([start])
    
    # Perform BFS
    while queue:
        current_word, depth = queue.popleft()
        
        # Try changing each letter of the current word
        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':  # Try replacing with each letter
                transformed_word = current_word[:i] + c + current_word[i+1:]
                
                # If we find the end word, return the depth (length of the transformation)
                if transformed_word == end:
                    return depth + 1
                
                # If the transformed word is in the word list and not visited yet, add it to the queue
                if transformed_word in wordList and transformed_word not in visited:
                    visited.add(transformed_word)
                    queue.append((transformed_word, depth + 1))
    
    # If no transformation sequence exists
    return 0

# Example usage:
start = "hit"
end = "cog"
wordList = {"hot", "dot", "dog", "lot", "log", "cog"}

print("Shortest transformation sequence length:", wordLadder(start, end, wordList))
