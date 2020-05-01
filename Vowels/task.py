vowels = 'aeiou'
# create your list here

letters = list(input())

vowel_in_word = [letter for letter in letters if letter in vowels]

print(vowel_in_word)
