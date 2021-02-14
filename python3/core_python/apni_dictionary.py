my_dictionary = {
    'python': "Guido van Rossum",
    'c': "Dennis Ritchie",
    "c++": "Bjarne Stroustrup",
    'java': 'James Gosling',
    'javascript': 'Brendan Eich',
    'dart': "Google",
    'go': 'Google',
    'kotlin': 'JetBrains'
}

key = input("Enter any programming language to know who is the creator : ").lower()
if key in my_dictionary.keys():
    print(my_dictionary.get(key))
else:
    print("Does not exist in the dictionary")