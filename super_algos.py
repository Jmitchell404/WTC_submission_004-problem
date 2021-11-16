import unittest
import sys
#check if empty or has no strings by tests
def find_min(element):
    """[This function finds and returns the minimum element in a list of intergers.
    Returns if the element paramater contains an invalid with a -1.]
    """
    if element == []:
        return -1

    if type(element[0]) == str:
        return -1

    if len(element) == 1:
        return element[0]
    else :
        if element[0] >= element[1]:
            del element[0]
            return find_min(element)
        elif element[0] <= element[1]:
            del element[1]
            return find_min(element)
    return element[0]


def sum_all(element):
    """[This function calculates and returns the sum of all element in a list of integers.
    Returns if the element paramater contains an invalid with a -1.]
    """
    if len(element)==1:
        return element[0]

    if len(element)==0:
        return -1

    if type(element[0]) != int:
        return -1
    else :
        element[0] += element[1]
        del element[1]
        sum_all(element)
    return element[0]


def find_possible_strings(char_set, k):
    """
    This function prints all of the possible strings of the length of k.
    """
    n = len(char_set)
    if not type(char_set) == list:
        return []
    
    for i in char_set:
        if type(i) != str:
            return []
    return possiblestringsRec(char_set, "", n, k, [])


def possiblestringsRec(char_set, prefix, n, k, new_list):
    """[Returns The function with the new list with 2 letters(a, b)]

    Argument:
        char_set : [how many intergers will be in the list]
        prefix : [contains the intergers(a,b,aa,bb,etc)]
        n : [length of the character_set]
        k : [equals 0]
        new_list : [empty list]

    Returns:
         [returns the empty list with intergers a,b till completion.]
    """
    if (k == 0) :
        new_list.append(prefix)
        return

    for i in range(n):
        newPrefix = prefix + (char_set[i])
        possiblestringsRec(char_set, newPrefix, n, k - 1, new_list)
    return new_list