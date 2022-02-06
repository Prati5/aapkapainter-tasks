def check_anagram(word1, word2):
    if sorted(word1.lower()) == sorted(word2.lower()):
        print("Yes")
    else:
        print("No")


check_anagram("Mary", "Army")