user_word = input("give me your first and last name: ")

vowels = ['a','e','i','o','u']
vowel_count = 0
specific_vowel = 0
x = []
def reverse_word(user_word):
    reverse_it = user_word[::-1]
    print(reverse_it)

def serperate_word(user_word):
    names = user_word.split(" ")
    print(names)

def total_vowel_count(user_word, vowels, vowel_count):
    for char in user_word:
        if char in vowels:
            vowel_count += 1
        else:
            continue
    return vowel_count

def specific_vowel(user_word, x, specific_vowel):
    specific_vowel = 0
    x = input('what vowel do you want to look for: ')
    for char in user_word:
        if char in x:
            specific_vowel += 1
        else: 
            continue
    return specific_vowel,x



serperate_word(user_word)
f'your name backwards is {reverse_word(user_word)}'
print(f'The amount of vowels in your name is {total_vowel_count(user_word, vowels, vowel_count)}')
print(f'you have {specific_vowel(user_word, x, specific_vowel)} {x}s in your name')
        


        
