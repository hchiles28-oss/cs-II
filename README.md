import random
user_word = input('name: ')

'''
List of Functions:
1. Reverse and display- done
2. Determine the number of vowels. You can prompt user for a particular vowel or
create subtotals of each.- done
3. Consonant frequency. - done Bonus: Subtotals of each consonant
4. Return first name. - done
5. Return last name. - done
6. Return middle name(s)- done
7. Return boolean if last name contains a hyphen- done
8. Function to convert to lowercase
9. Function to convert to uppercase
10. Modify array to create a random name (mix up letters)- done
11. Return boolean if first name is a palindrome - done
12. Return full-name as a sorted array of characters (Bonus)
13. Build a menu (Bonus) - NEED TO DO
14. Make initials from name - NEED TO DO
15. Return boolean if name contains a title/distinction (“Dr.”, “Sir”, “Esq”, “Ph.d”)
(Bonus)
'''
user_word = input("give me your first and last name: ")
import random
vowels = ['a','e','i','o','u','y']
vowel_count = 0
specific_vowel = 0

vowel_user_wants = []

def reverse_word(user_word):

    """Reverses and prints the input string.

    Args:
        user_word (string): The string to be reversed.
    """
    reverse_it = user_word[::-1]
    print(reverse_it)

def first_name (user_word):

    """Extracts and prints the first name from a space-separated full name string.

    Args:
        user_word (str): A space-separated string containing names.
    """

    names = user_word.split(" ")
    first_name = names[0]
    print(first_name)

def middle_name (user_word):

    """Extracts and prints middle name(s) if more than two names are provided.

    Args:
        user_word (str): A space-separated string containing names.
    """

    names = user_word.split(" ")
    ln = len(names)
    if ln > 2:
        names.pop(0)
        names.pop()
        print(names)
    
def last_name (user_word):

    """Extracts and prints the last name from a space-separated full name string.

    Args:
        user_word (str): A space-separated string containing names.
    """

    names = user_word.split(" ")
    ln = len(names)
    last_name = names[ln-1]
    print(last_name)

def hyphen_check(user_word):

    """Checks whether the input string contains a hyphen and prints the result.

    Args:
        user_word (str): The string to inspect for hyphens.
    """

    if '-' in user_word:
        print("you have a hyphen in your name: ")
    else:
        print("you don't have a hypen in your name: ")

def total_vowel_count(user_word, vowels, vowel_count):

    """Calculates the total number of vowels present in the input string.

    Args:
        user_word (str): The input string to evaluate.
        vowels (list of str): A list of characters recognized as vowels.
        vowel_count (int): The starting counter value.

    Returns:
        int: The updated total count of vowels found.
    """

    for char in user_word:
        if char in vowels:
            vowel_count += 1
        else:
            continue
    return vowel_count

def specific_vowels(user_word, vowel_user_wants, specific_vowel):

    """Prompts the user for a specific vowel and counts its occurrences in their name.

    Args:
        user_word (string): The string to search through.
        vowel_user_wants (string): Variable to store user input vowel choice.
        specific_vowel (int): The initial count variable.

    Returns:
        - specific_vowel (int): Total occurrences of the selected vowel.
        - vowel_user_wants (str): The chosen vowel character.
    """

    specific_vowel = 0
    vowel_user_wants = input('what vowel do you want to look for: ')
    for char in user_word:
        if char in vowel_user_wants:
            specific_vowel += 1
        else: 
            continue
    return specific_vowel,vowel_user_wants

def consonant_frequency(user_word):

    """Counts and prints the total number of consonants in the input string.

    Args:
        user_word (str): The string to break down for consonants.
    """

    letters = list(user_word)
    consonant_count = 0
    consonants = [
    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z',
    'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'
]
    for letter in letters:
        if letter in consonants:
            consonant_count += 1
    print(consonant_count)

def palindrome_check(user_word):

    """Checks if the first name is a palindrome.

    Args:
        user_word (str): A space-separated list of the names, but only for first one.
    """

    split_names = user_word.split(" ")
    first_name_palindrome = split_names.pop(0)
    palindrome = first_name_palindrome[::-1]
    if palindrome == first_name_palindrome:
        print("your first name is a palindrome: ")
    else:
        print("your name is not a palindrome: ")
 
def scrambled_word(user_word):

    """Randomly shuffles the characters in the input string.

    Args:
        user_word (str): The string to scramble.

    Returns:
        str: A new string with characters in randomized order.
    """
    
    scramble = "".join(random.sample(user_word, len(user_word)))
    return(scramble)

#def lower_case(user_word):
    

def main(user_word, vowels, vowel_count, specific_vowel,vowel_user_wants):
    user_choice = input('which function would you like to call? ' \
    '1. First Name. ' \
    '2. Middle name. ' \
    '3. Last name. ' \
    '4. reverse your name. ' \
    '5. see if your name has a hyphen. ' \
    '6. see how many vowels are in your name. ' \
    '7. find the count of a specific vowel. ' \
    '8. see how many consonants you have in your name. ' \
    '9. see if your first name is a palindrome. ' \
    '10. Scramble your name into a random set of letters.'
    '11. Exit the code ')
    while True:
        if user_choice == 1: 
            first_name(user_word)
        elif user_choice == 2:
            middle_name(user_word)
        elif user_choice == 3:
            last_name(user_word)
        elif user_choice == 4:    
            reverse_word(user_word)
        elif user_choice == 5:   
            hyphen_check(user_word)
        elif user_choice == 6:    
            total_vowel_count(user_word, vowels, vowel_count)
        elif user_choice == 7:   
            specific_vowels(user_word, vowel_user_wants, specific_vowel)
        elif user_choice == 8:   
            consonant_frequency(user_word)
        elif user_choice == 9:    
            palindrome_check(user_word)
        elif user_choice == 10:   
            scrambled_word(user_word)
        elif user_choice == 11:
            break 
        else:
            return ValueError

main(user_word, vowels, vowel_count, specific_vowel,vowel_user_wants)
