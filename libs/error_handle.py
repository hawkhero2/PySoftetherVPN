#! /usr/bin/env python3

def has_error(input :list) ->list:
    """Check if error is empty string

    Args:
        input (list): Input list of strings

    Returns:
        bool: True if error is empty string
    """
    result= [False,"", ""]
    
    for line in input:
        index=0
        if(line.__contains__("Error code")):
            result[0] = True
            result[1] = input[index]
            result[2] = input[index+1]
            break
        else:
            index=index+1

    return result
