# T9dictionary
Implementation of T9 dictionary in python

T9, which stands for Text on 9 keys, is a patented predictive text technology for mobile phones, originally developed by Tegic Communications, now part of Nuance Communications.

T9's objective is to make it easier to enter text messages. It allows words to be formed by a single keypress for each letter, which is an enormous improvement over the multi-tap approach used in conventional mobile phone text entry at the time, in which several letters are associated with each key, and selecting one letter often requires multiple keypresses.

T9 combines the groups of letters on each phone key with a fast-access dictionary of words. It will then look up in the dictionary all words corresponding to the sequence of keypresses and order them by frequency of use. As T9 "gains familiarity" with the words and phrases the user commonly uses, it speeds up the process by offering the most frequently used words first and then letting the user access other choices with one or more presses of a predefined "Next" key.

<img width="362" alt="Screen Shot 2021-06-22 at 11 13 38 PM" src="https://user-images.githubusercontent.com/54487818/123029701-85a73f00-d3af-11eb-8938-f7d90f042716.png">

I have implemented the T9 dictionary for the purpose of searching for potential phone contacts based on the input given from the 9 keys. I have not incorporated frequency of searches into the algorithm. This is the base level implementation of T9. 

Contact names have been randomly generated using the generate_random_strings.py file. The dictionary is created after the contacts have been loaded in and based on the input from the keypad, all the possible contacts are printed.
