# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word_list = list(word)
    anagram_list = list(anagram)

    if len(word_list) != len(anagram_list):
        return False

    if sorted(anagram_list) != sorted(word_list):
        return False
    
    return True


if __name__ == '__main__':
    print(find_anagram("below", "elbow"))
    print(find_anagram("hello", "check"))