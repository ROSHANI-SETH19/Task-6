def word_frequency(text):
    # Normalize the text by converting it to lowercase
    text = text.lower()
    
    # Split the text into words (default split() splits by spaces)
    words = text.split()
    
    # Create an empty dictionary to store word counts
    word_count = {}
    
    # Count the frequency of each word
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

# Example usage
text = "Hello world! Hello everyone. The world is beautiful."
word_counts = word_frequency(text)
print(word_counts)
