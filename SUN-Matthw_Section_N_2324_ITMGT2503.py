General Instructions
Change the filenames to LastName-FirstName_Section_M-N_2324_ITMGT2503
Ex. GAW-Adriel_SectionM_2324_ITMGT2503

Question 1: Watch Your Words
Your task is to count the number of times that each word was used in a movie script! Please be guided by the instructions below!

1a

# First, to help guide you, here is a list containing tuples. Run this block of code to initialize the list
list_of_tuples = [('A',59),('B',100),('C',20),('D',88),('E',25),('F',38)]

list_of_tuples

If we want to sort this tuple according to the numerical value, using the sort() without any other arguments will not suffice. But, diving a bit deeper into the sort() function, we can see that it can accept two parameters:

key which is what will be used as the basis for sorting
reverse which accepts a Boolean value to determine if the sorting will be ascending or descending

# execute this cell to see how the two arguments help us achieve the desired result

list_of_tuples.sort(key=lambda x: x[1], reverse=True)

print(list_of_tuples)

1b

# To formally start this problem:
# Load the "script.json" file and store it in the `jsondata` variable. 
# The dictionary will contain the "line number" (starting from 0) as the key, 
# and the lines itself as the value

import json
import numpy as np
import pandas as pd

jsondata = pd.read_json("script.json",typ="dictionary").sort_values()

1c 

# To process the lines in the script, you need to do the following in chronological order:
#### Convert all characters to uppercase characters
#### Remove the following pieces of text: <P>, </P>, <B>, </B>, <I>, </I>
#### Remove all the unnecessary punctuation symbols denoted in the string below
unnecessary_punctuation = r"&$@[].,'#()-\"!?’_;:/"

print(type(jsondata)
jsonstring = json.dumps(jsondata)  
jsonstring += jsonstring.upper()

for jsonstring:
if jsonstring.find("<P>") == TRUE:
    jsonstring.replace("<P>","",1)
elif jsonstring.find("</P>") == TRUE:
    jsonstring.replace("</P>","",1)
elif jsonstring.find("<B>") == TRUE:
    jsonstring.replace("<B>","",1)
elif jsonstring.find("</B>") == TRUE:
    jsonstring.replace("</B>","",1)
elif jsonstring.find("<I>") == TRUE:
    jsonstring.replace("<I>","",1)
elif jsonstring.find("</I>") == TRUE:
    jsonstring.replace("</I>","",1)
else:
 if jsonstring.find("&") == TRUE:
    jsonstring.replace("&"," ",1)
    elif jsonstring.find("$") == TRUE:
    jsonstring.replace("$"," ",1)
    elif jsonstring.find("@") == TRUE:
    jsonstring.replace("@"," ",1)
    elif jsonstring.find("[") == TRUE:
    jsonstring.replace("["," ",1)
    elif jsonstring.find("]") == TRUE:
    jsonstring.replace("]"," ",1)
    elif jsonstring.find(".") == TRUE:
    jsonstring.replace("."," ",1)
    elif jsonstring.find(",") == TRUE:
    jsonstring.replace(","," ",1)
    elif jsonstring.find("'") == TRUE:
    jsonstring.replace("'"," ",1)
    elif jsonstring.find("#") == TRUE:
    jsonstring.replace("#"," ",1)
    elif jsonstring.find("(") == TRUE:
    jsonstring.replace("("," ",1)
    elif jsonstring.find(")") == TRUE:
    jsonstring.replace(")"," ",1)
    elif jsonstring.find("-") == TRUE:
    jsonstring.replace("-"," ",1)
    elif jsonstring.find('"') == TRUE:
    jsonstring.replace('"'," ",1) 
    elif jsonstring.find("!") == TRUE:
    jsonstring.replace("!"," ",1) 
    elif jsonstring.find("?") == TRUE:
    jsonstring.replace("?"," ",1) 
    elif jsonstring.find("’") == TRUE:
    jsonstring.replace("’"," ",1)
    elif jsonstring.find("_") == TRUE:
    jsonstring.replace("_"," ",1)
    elif jsonstring.find(";") == TRUE:
    jsonstring.replace(";"," ",1)
    elif jsonstring.find(":") == TRUE:
    jsonstring.replace(":"," ",1)
    elif jsonstring.find("/") == TRUE:
    jsonstring.replace("/"," ",1)
    elif jsonstring.find('"') == TRUE:
    jsonstring.replace('"'," ",1)
    elif jsonstring.find("\") == TRUE:
    jsonstring.replace("\"," ",1) 
    else:
        result jsonstring

1d

# From here, create a dictionary called `wordcount_dictionary` that will have the key:value pair of word:count
# But, only include words that are three (3) letters or more

print(wordcount_dictionary)
for k, v in wordcount_dictionary.items():
    print(k, v)
    del wordcount_dictionary(len <= 3)
    
COUNT_THE = jsonstring.count(THE)
COUNT_JOY = jsonstring.count(JOY)
COUNT_AND = jsonstring.count(AND)
COUNT_RILEY = jsonstring.count(RILEY)
COUNT_SADNESS = jsonstring.count(SADNESS)

wordcount_dictionary = {"THE": COUNT_THE, "JOY": COUNT_JOY, "AND": COUNT_AND, "RILEY": COUNT_RILEY, "SADNESS": COUNT_SADNESS

1e

# Afterwards, we want to convert that dictionary to a list containing tuples
# Create a list called "final_wordlist_of_tuples" containing tuples 
# Each tuple should be as follows: (word,count)
# Sort the list by `count` (the second element of the tuple) in descending order
# A correct sample is shown in the markdown cell below
# Hint: this can be done using lambda but you can use a regular function definition. 
# Make sure you go through the mini-tutorial at the start of this problem.

final_wordlist_of_tuples  = [("THE", COUNT_THE), ("JOY", COUNT_JOY), ("AND", COUNT_AND), ("RILEY", COUNT_RILEY), ("SADNESS", COUNT_SADNESS)]
sorted_list = sorted(final_wordlist_of_tuples.count())

Question 2: Wait... What is LP Doing Here?
I swear you don't need to do LP here. In fact, the LP formulation is already shown below!

LP Problem
In the realm of Sanctoria, nestled deep within the misty forests and craggy mountains, lies the legendary dungeon of The Lost King. It is said to be filled with untold riches, ancient relics, and formidable monsters guarding its treasures. As the wise and benevolent ruler of Sanctoria, King Hexter has decided to assemble a daring raiding party to plunder the depths of the dungeon and reclaim its treasures for the kingdom.

As the illustrious ruler of Sanctoria, King Hexter is faced with the daunting task of assembling a formidable dungeon raiding party. The success of the raid hinges upon the careful selection and allocation of resources to hire Fighters, Rangers, and Clerics for the expedition into the depths of the Lost King’s home.

In the planning of this dungeon raid, the King’s advisors have provided him with the following: Gold: The kingdom's treasury can afford to spend no more than 18000 gold coins on hiring adventurers. Each Fighter costs 1000 gold coins, each Ranger costs 600 gold coins, and each Cleric costs 750 gold coins. Lumber: The construction of necessary equipment for each troop requires ample quality lumber. The kingdom has 12000 units of lumber available for the raid. Each Fighter requires 500 units, each Ranger requires 750 units, and each Cleric requires 300 units. Food: The raid will last several weeks so food must be kept and stored during the raid. The raid will be able to carry 1500 units of food available for the raid. Each Fighter requires 50 units, each Ranger requires 45 units, and each Cleric requires 75 units. Power: The power of the raiding party will dictate the level of the raid’s success. Each Fighter gives 10 points, each Ranger gives 12 points, each Cleric gives 16 points.

The King’s military advisors have also discussed strategies that will be employed in the raid: Having more Fighters than Rangers will bolster the raiding party's frontline defense To avoid casualties, each Cleric must have at most 3 Fighters that they are supporting

LP Formulation
Decision Variables:

(F): Number of Fighters
(R): Number of Rangers
(C): Number of Clerics
Objective: Maximize the power of the raiding party.


Subject to:

# With the LP Formulation as a basis, find the optimal solution to the problem using Python
# Use the variable `optimal_Z` to store the value of the Maximum Z
# Use the variables `optimal_F`, `optimal_R`, and `optimal_C` to store 
# the optimal solution of Fighters, Rangers, and Clerics respectively
# Note: There may be multiple configurations of F, R, C to attain the Maximum Z. 
# Hint: Don't use your DecSci brain, use your Python programming brain

def Party_Power(optimal_F,optimal_R,optimal_C):
    optimal_F >= 0
    optimal_R >= 0
    optimal_C >= 0
    (1000 * optimal_F) + (600 * optimal_R) + (750 * optimal_C) <= 18000
    (500 * optimal_F) + (750 * optimal_R) + (300 * optimal_C) <= 12000
    (50 * optimal_F) + (45 * optimal_R) + (75 * optimal_C) <= 1500
    

    #range is 20 because maximum number of total party members is 20 * 75 <= 1500 (Food constraint)
    for optimal_F, optimal_R, optimal_C in range(20):
        if (10 * optimal_F) + (12 * optimal_R) + (16 * optimal_C) > (10 * (optimal_F + 1)) + (12 * (optimal_R + 1)) + (16 * (optimal_C + 1)) and (10 * optimal_F) + (12 * optimal_R) + (16 * optimal_C) > (10 * (optimal_F - 1)) + (12 * (optimal_R - 1)) + (16 * (optimal_C - 1)):
            optimal_z = (10 * optimal_F) + (12 * optimal_R) + (16 * optimal_C)
            return optimal_Z
 	    break
        else:
            optimal_F += optimal_F + 1
            optimal_R += optimal_R + 1
            optimal_C += optimal_C + 1

# If there were no errors in the way you processed your data, 
# this should output "Looks Good!"  

assert optimal_Z == 344
assert (1000*optimal_F + 600*optimal_R + 750*optimal_C) <= 18000
assert (500*optimal_F + 750*optimal_R + 300*optimal_C) <= 12000
assert (50*optimal_F + 45*optimal_R + 75*optimal_C) <= 1500
print("Looks Good!")

Question 3: Collatz

3a

The Collatz Conjecture is a mathematical sequence defined as follows:

Start with any positive integer n.
If n is even, divide it by 2 to get n / 2.
If n is odd, multiply it by 3 and add 1 to get 3n + 1.
Repeat the process with the resulting number.
The conjecture states that no matter which positive integer you start with, you will always eventually reach 1.
As an example, the number 5 will follow this sequence:

Start at 5
5 is odd, so we multiply by 3 and adds 1 to get 16
16 is even, so we divide by 2 to get 8
8 is even, so we divide by 2 to get 4
4 is even, so we divide by 2 to get 2
2 is even, so we divide by 2 to get 1
Since the number is 1, we stop the sequence.
For the purposes of this problem, let's call the list containing the numbers [5, 16, 8, 4, 2, 1] the Collatz Sequence.


This sequence also has a Collatz Length of 6, since the sequence cycled through 6 numbers.

The sequence also had a Max Collatz of 16, since that was the highest number in the sequence.

Lastly, the sequence had a Sequence Sum of 36, since that is the sum of all the numbers in the sequence.

def Collatz(start_number):
    '''
    Create a SINGLE FUNCTION that will return the
    `Collatz Sequence`, the `Collatz Length`,
    and the `Max Collatz` in a dictionary.

    The key-value pairs will be the following:
    "collatz_sequence": the list containing the numbers of the sequence
    "collatz_length": the length of the sequence
    "max_collatz": the maximum number achieved in the sequence
    "sequence_sum": the sum of all the numbers in the sequence 

    Parameters
    ----------
    start_number: int
        the number used to start the sequence

    Returns
    -------
    dictionary
        the dictionary containing the key-value pairs of the
        collatz_sequence, collatz_length, max_collatz, and sequence_sum
    '''
start_number = i
collatz_sequence = []

while start_number != 1:
        if start_number % 2 == 0:
            n_divided_by_two = start_number // 2
            start_number += n_divided_by_two
            collatz_sequence.append(start_number)
            collatz_length = count(collatz_sequence)
            max_collatz = max(collatz_sequence)
            sequence_sum = sum(collatz_sequence)
        else:
            odd_n = (3 * start_number) + 1
            odd_n += start_number
            collatz_sequence.append(start_number)
            collatz_length = count(collatz_sequence)
            max_collatz = max(collatz_sequence)
            sequence_sum = sum(collatz_sequence)
key_value_pair_list = { "collatz_sequence": collatz_sequence,
                       "collatz_length": collatz_length,
                       "max_collatz": max_collatz
                       "sequence_sum": sequence_sum
}
return key_value_pair_list

3b 

def Collatz_winner(number_list):
    '''
    Given a list of positive integers, return the `winner`
    among them. The `winner` is categorized as such:
        
        1. The number has the largest `collatz_length`; and
        2. The number has the largest `max_collatz`

    If there is no winner, then the function must return None

    Parameters
    ----------
    number_list: list
        a list of positive integers

    Returns
    -------
    integer (or NoneType)
        the "winner" that follows the specific criteria above
        returns a None if it does not meet all the criteria above
    '''
    for i in number_list[1:i]:
    if key_value_pair_list(collatz_length(number_list)) > key_value_pair_list(collatz_length(number_list + 1)) and    key_value_pair_list(max_collatz(number_list)) > key_value_pair_list(max_collatz(number_list))
    max(collatz_length(number_list):
        result number_list
        break
    elif key_value_pair_list(collatz_length(number_list)) < key_value_pair_list(collatz_length(number_list + 1)) and key_value_pair_list(max_collatz(number_list)) < key_value_pair_list(max_collatz(number_list))
    max(collatz_length(number_list):
        number_list += number_list + 1
    else:
        result print('None')
        break

assert Collatz_winner(range(1,51)) == 27
assert Collatz_winner(range(1,10)) == 9
assert Collatz_winner(range(50,100)) == 97
assert Collatz_winner(range(50,100,4)) == 54
assert Collatz_winner(range(20,131,5)) == 110
assert Collatz_winner(range(75,180,9)) == 129

 

