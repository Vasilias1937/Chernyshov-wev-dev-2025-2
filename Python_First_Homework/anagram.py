from collections import Counter

str1 = input()

str2 = input()

def are_anagrams(str1, str2):
    counter1 = Counter(str1)
    counter2 = Counter(str2)

    return counter1 == counter2

if are_anagrams(str1, str2):
    print("True")
else:
    print('False')