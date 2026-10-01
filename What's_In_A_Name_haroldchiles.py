'''
Name: Harold Chiles

Description: This is a program where the main function slices and dices
your name, and can contort it in many ways. The goal is to manipulate strings.

Bugs: During running I did not encounter any bugs I could not solve, but one
item I want to bring up is that while valueError ends the code effectively it
does not give the user another chance to continue.

Bonus: I wrote a menu for easy use

Log: 9/30/2026 by Harold chiles
'''
user_word = input("give me your name: ")
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

def lower_case(user_word):

    """
    Description: Converts all uppercase characters in a string to lowercase and
    leaves non-uppercase characters unchanged.

    Parameters:
    - user_word: the string to convert to lowercase

    Returns:
    - str: the resulting lowercase string
    """

    lower_name = []
    for i in user_word:
        if 65<= ord(i) <= 90:                           #ord refers back to a characterized list of python letter translations
            newletter1 = ord(i) + 32
            newletter = chr(newletter1)
            lower_name.append(newletter)
        else:
            lower_name.append(i)

    lower_name_final = "".join(lower_name)

    return lower_name_final

def upper_case(user_word):

    """
    Description: Converts all lowercase characters in a string to uppercase 
    and leaves non-lowercase characters unchanged.

    Parameters:
    - user_word: the string to convert to uppercase

    Returns:
    - str: the end uppercase string
    """

    upper_name = []
    for i in user_word:
        if 97<= ord(i) <= 122:                    #ord refers back to a characterized list of python letter translations
            newletter1 = ord(i) + 32
            newletter1 = ord(i) - 32
            newletter = chr(newletter1)
            upper_name.append(newletter)
        else:
            upper_name.append(i)
    
    upper_name_final = "".join(upper_name)
    
    return upper_name_final

def initials(user_word):

    """
    Description: Extracts the first character from each word in a string 
    and combines them into a single string.

    Parameters:
    - user_word: a string representing a full name

    Returns:
    - str: a string composed of the first letter of each word
    """

    Initial_list = []
    names = user_word.split(" ")
    ln = len(names)
    for name in names:
        Initial_list.append(name[0])
        
    initial_final = "".join(Initial_list)

    return initial_final

        
def main(user_word, vowels, vowel_count, specific_vowel,vowel_user_wants):

    """
    Description: A menu is presented that compiles many different functions
    a user could want to use. There are a total of 14 options

    Parameters:
    - user_word: the string input to be processed by menu selections
    - vowels: a list of vowels 
    - vowel_count: a place to keep track of vowel count
    - specific_vowel: keeps track of how many times the vowel the user wants comes up
    - vowel_user_wants: the specific vowel selected

    Returns:
    - None: exits the loop when menu choice 14 is selected (or returns ValueError on invalid menu options)
    """


    while True:
        user_choice1 = input('''which function would you like to call? 
        1. First Name. 
        2. Middle name. 
        3. Last name. 
        4. reverse your name. 
        5. see if your name has a hyphen.  
        6. see how many vowels are in your name. 
        7. find the count of a specific vowel. 
        8. see how many consonants you have in your name. 
        9. see if your first name is a palindrome. 
        10. Scramble your name into a random set of letters.
        11. Make your name lowercase
        12. Make your name uppercase
        13. Initials
        14. Exit
          ''')
        user_choice = int(user_choice1)
    
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
            print(total_vowel_count(user_word, vowels, vowel_count))
        elif user_choice == 7:   
            print(specific_vowels(user_word, vowel_user_wants, specific_vowel))
        elif user_choice == 8:   
            consonant_frequency(user_word)
        elif user_choice == 9:    
            palindrome_check(user_word)
        elif user_choice == 10:   
            print(scrambled_word(user_word))
        elif user_choice == 11:
            print(lower_case(user_word))
        elif user_choice == 12:
            print(upper_case(user_word))
        elif user_choice == 13:
            print(initials(user_word))
        elif user_choice == 14:
            break
        else:
            return ValueError
            

main(user_word, vowels, vowel_count, specific_vowel,vowel_user_wants)
