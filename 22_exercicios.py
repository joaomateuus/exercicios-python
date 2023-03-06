"""
ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
"""
def animal_crackers(words: str):
    word = words.split(' ')
    if word[0][0] == word[1][0]:
        return True
    else:
        return False
result = animal_crackers('Cavalo Louco')
print(result)