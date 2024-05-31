def word_counter(text):
    try:
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")    
        text = text.strip()      
        if not text:
            return 0
        words = text.split()
        return len(words)
    except TypeError as e:
        
        print("Error:", e)
        return -1
input_text = "This is a sample text for word counting."

count = word_counter(input_text)
    
if count != -1:
    print("Number of words:", count)