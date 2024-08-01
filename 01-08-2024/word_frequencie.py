def word_frequencies(text):
 
    text = text.lower()
    for char in "-.,\n":
        text = text.replace(char, " ")
    
 
    words = text.split()
    
    freq_dict = {}
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    
    return freq_dict

user_text = input("Enter a string of text: ")
frequencies = word_frequencies(user_text)
print(frequencies)
