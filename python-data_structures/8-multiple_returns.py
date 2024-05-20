#!/usr/bin/python3
def multiple_returns(sentence):
    """
    Function returns a tuple with the length of a string and its first character.
    
    Args:
        sentence (str): The input sentence.
    
    Returns:
        tuple: A tuple containing two elements.
            - First element: Length of the string
            - Second element: First character of the string.
            If the input sentence is an empty string, the second element of the tuple will be None.
    """
    new_list = []
    new_list.append(len(sentence))
    if sentence == "":
        new_list.append(None)
    else:
        new_list.append(sentence[0])
    new_tuple = tuple(new_list)
    return new_tuple

