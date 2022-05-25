# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, encoding="utf-8") as f:
        return f.read()
            
def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    word_count = dict()
    text = text.lower().split(" ")
    text = [word for word in text if len(word)]

    for (i, word) in enumerate(text):
        word_list = list(word)
        if word_list[0] == '\n':
            del word_list[0]
            # text[index] = ''.join(word_list)
        for (j, char) in enumerate(word_list):
            if not char.isalpha():
                del word_list[j]
            text[i] = ''.join(word_list)

    
    for word in text:
        if word in word_count:
            word_count[word] +=1
        else:
            word_count[word] = 1

    return word_count


if __name__ == '__main__':
    print(count_words())
